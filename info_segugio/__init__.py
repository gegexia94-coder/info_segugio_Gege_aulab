import chainlit as cl

# Questa è la prima versione dell'app.
# Per ora non usiamo ancora OpenAI o Tavily.
# Prima controllo solo che Chainlit risponda nel browser.

@cl.on_message
async def main(message: cl.Message):
    testo_utente = message.content

    await cl.Message(
        content=f"Info Segugio è pronto. Hai scritto: {testo_utente}"
    ).send()
