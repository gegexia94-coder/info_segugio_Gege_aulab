import json
from openai import OpenAI

from info_segugio.config import Config
from info_segugio.prompts import (
    build_search_query_prompt,
    build_final_answer_prompt,
    build_reflection_prompt,
)

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def ask_openai(user_prompt: str) -> str:
    response = client.responses.create(
        model=Config.OPENAI_MODEL,
        input=user_prompt,
    )
    return response.output_text.strip()


def generate_search_query(user_question: str) -> str:
    prompt = build_search_query_prompt(user_question)
    return ask_openai(prompt)

def generate_reflection(query: str, summary: str) -> dict:
    prompt = build_reflection_prompt(query, summary)
    answer = ask_openai(prompt)

    try:
        return json.loads(answer)
    except json.JSONDecodeError:
        return {
            "needs_more_search": False,
            "reason": "Risposta reflection non valida in JSON.",
            "next_query": "",
        }


def generate_final_answer(user_question: str, results: list[dict]) -> str:
    prompt = build_final_answer_prompt(user_question, results)
    return ask_openai(prompt)
