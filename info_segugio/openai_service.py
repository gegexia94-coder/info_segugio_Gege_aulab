from openai import OpenAI

from info_segugio.config import Config
from info_segugio.prompts import (
    build_search_query_prompt,
    build_final_answer_prompt,
)

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def generate_search_query(user_question: str) -> str:
    prompt = build_search_query_prompt(user_question)

    response = client.responses.create(
        model=Config.OPENAI_MODEL,
        input=prompt,
    )

    return response.output_text.strip()

def generate_final_answer(user_question: str, results: list[dict]) -> str:
    prompt = build_final_answer_prompt(user_question, results)

    response = client.responses.create(
        model=Config.OPENAI_MODEL,
        input=prompt,
    )

    return response.output_text.strip()
