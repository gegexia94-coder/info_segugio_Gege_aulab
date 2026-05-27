from info_segugio.openai_service import (
    generate_search_query,
    generate_final_answer,
)
from info_segugio.tavily_service import search_web

def run_search_flow(user_question: str) -> dict:
    search_query = generate_search_query(user_question)
    results = search_web(search_query, max_results=3)

    final_answer = generate_final_answer(user_question, results)

    return {
        "question": user_question,
        "query": search_query,
        "results": results,
        "answer": final_answer,
    }
