from openai import OpenAI

from info_segugio.config import Config
from info_segugio.prompts import build_search_query_prompt

# Qui preparo il client OpenAI.
# La chiave arriva da Config, quindi dal file .env.
client = OpenAI(api_key=Config.OPENAI_API_KEY)

def generate_search_query(user_question: str) -> str:
    prompt = build_search_query_prompt(user_question)

    response = client.responses.create(
        model=Config.OPENAI_MODEL,
        input=prompt,
    )

    return response.output_text.strip()
