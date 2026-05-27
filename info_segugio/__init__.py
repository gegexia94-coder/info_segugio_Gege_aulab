import chainlit as cl

from info_segugio.search_pipeline import run_search_flow

# Questo è il punto di ingresso della chat.
# Chainlit chiama questa funzione quando l'utente scrive.

def format_result(item: dict) -> str:
    title = item.get("title", "Titolo non disponibile")
    url = item.get("url", "")
    content = item.get("content", "")[:350]

    return f"### {title}\n{url}\n\n{content}"

@cl.on_message
async def main(message: cl.Message):
    user_question = message.content

    await cl.Message(
        content="Sto preparando la ricerca..."
    ).send()

    data = run_search_flow(user_question)

    sources = []
    for item in data["results"]:
        sources.append(format_result(item))

    answer = "\n\n---\n\n".join(sources)

    await cl.Message(
        content=f"""
## Info Segugio

**Domanda:** {data["question"]}

**Query usata:** `{data["query"]}`

**Fonti trovate:** {len(data["results"])}

---

{answer}
"""
    ).send()
