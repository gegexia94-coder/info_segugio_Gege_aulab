import traceback
import chainlit as cl

from info_segugio.openai_service import (
    generate_search_query,
    generate_reflection,
    generate_final_answer,
)
from info_segugio.tavily_service import search_web
from info_segugio.search_pipeline import (
    remove_duplicate_sources,
    build_fallback_query,
    MIN_SEARCH_ROUNDS,
    MAX_SEARCH_ROUNDS,
    RESULTS_PER_SEARCH,
)


def format_source(item: dict) -> str:
    title = item.get("title", "Titolo non disponibile")
    url = item.get("url", "")
    return f"- [{title}]({url})"


@cl.on_message
async def main(message: cl.Message):
    user_question = message.content
    search_steps = []
    all_results = []

    try:
        await cl.Message(
            author="system_assistant",
            content="Sto preparando una query di ricerca ottimizzata..."
        ).send()

        query = generate_search_query(user_question)

        await cl.Message(
            author="system_assistant",
            content=f"### Query iniziale ottimizzata\n`{query}`"
        ).send()

        for round_number in range(1, MAX_SEARCH_ROUNDS + 1):
            await cl.Message(
                author="system_assistant",
                content=f"### Giro {round_number}\nCerco sul web con:\n`{query}`"
            ).send()

            results = search_web(query, max_results=RESULTS_PER_SEARCH)
            all_results.extend(results)

            partial_results = remove_duplicate_sources(all_results)
            summary = generate_final_answer(user_question, partial_results)
            reflection = generate_reflection(query, summary)

            step = {
                "round": round_number,
                "query": query,
                "reflection": reflection,
                "results_found": len(results),
            }
            search_steps.append(step)

            next_query = reflection.get("next_query", "")
            reason = reflection.get("reason", "Motivo non disponibile")

            await cl.Message(
                author="system_assistant",
                content=f"""
### Risultato giro {round_number}

- Risultati trovati: **{len(results)}**
- Motivo nuova ricerca: {reason}
- Prossima query: `{next_query or "non necessaria"}`
"""
            ).send()

            if round_number >= MIN_SEARCH_ROUNDS and not reflection.get("needs_more_search"):
                break

            query = next_query or build_fallback_query(
                user_question,
                round_number + 1,
            )

        final_results = remove_duplicate_sources(all_results)
        answer = generate_final_answer(user_question, final_results)
        sources = "\n".join(format_source(item) for item in final_results)

        steps_text = "\n".join(
            f"- Giro {step['round']}: `{step['query']}` "
            f"({step.get('results_found', 0)} risultati)"
            for step in search_steps
        )

        await cl.Message(
            author="info_segugio",
            content=f"""
## Risposta finale Info Segugio

{answer}

---

### Ricerche automatiche eseguite
{steps_text}

### Fonti finali
{sources}
"""
        ).send()

    except Exception as error:
        error_log = traceback.format_exc()
        print(error_log)

        await cl.Message(
            author="system_assistant",
            content=f"""
## Errore durante la ricerca

Tipo errore: `{type(error).__name__}`

Messaggio:
`{error}`

Controlla il terminale: ora l'errore completo viene stampato nei log.
"""
        ).send()
