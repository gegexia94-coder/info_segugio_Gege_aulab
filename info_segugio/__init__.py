import chainlit as cl

from info_segugio.search_pipeline import run_search_flow

def format_source(item: dict) -> str:
    title = item.get("title", "Titolo non disponibile")
    url = item.get("url", "")
    return f"- [{title}]({url})"

def format_search_step(step: dict) -> str:
    reflection = step.get("reflection", {})

    text = f"- Giro {step['round']}: `{step['query']}`"
    text += f"\n  - Risultati trovati: {step.get('results_found', 0)}"

    reason = reflection.get("reason", "Motivo non disponibile")
    next_query = reflection.get("next_query", "")

    text += f"\n  - Motivo nuova ricerca: {reason}"

    if next_query:
        text += f"\n  - Prossima query: `{next_query}`"

    return text


@cl.on_message
async def main(message: cl.Message):
    user_question = message.content

    await cl.Message(
        author="info_segugio",
        content="Sto facendo una ricerca iterativa..."
    ).send()

    data = run_search_flow(user_question)

    steps = "\n".join(format_search_step(step) for step in data["search_steps"])
    sources = "\n".join(format_source(item) for item in data["results"])

    await cl.Message(
        author="info_segugio",
        content=f"""
## Risposta Info Segugio

{data["answer"]}

---

### Ricerche automatiche eseguite
{steps}

### Fonti finali
{sources}
"""
    ).send()
