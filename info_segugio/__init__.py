import chainlit as cl

from info_segugio.search_pipeline import run_search_flow

def format_source(item: dict) -> str:
    title = item.get("title", "Titolo non disponibile")
    url = item.get("url", "")
    return f"- [{title}]({url})"

@cl.on_message
async def main(message: cl.Message):
    user_question = message.content

    await cl.Message(content="Sto cercando fonti affidabili...").send()

    data = run_search_flow(user_question)
    sources = "\n".join(format_source(item) for item in data["results"])

    await cl.Message(
        content=f"""
## Risposta Info Segugio

{data["answer"]}

---

**Query usata:** `{data["query"]}`

**Fonti trovate:** {len(data["results"])}

{sources}
"""
    ).send()
