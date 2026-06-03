from info_segugio.openai_service import (
    generate_search_query,
    generate_reflection,
    generate_final_answer,
)
from info_segugio.tavily_service import search_web


def remove_duplicate_sources(results: list[dict]) -> list[dict]:
    seen_urls = set()
    unique_results = []

    for item in results:
        url = item.get("url")
        if url and url not in seen_urls:
            seen_urls.add(url)
            unique_results.append(item)

    return unique_results

def run_search_flow(user_question: str) -> dict:
    search_steps = []
    all_results = []

    query = generate_search_query(user_question)

    for round_number in range(1, 3):
        results = search_web(query)
        all_results.extend(results)

        step = {
            "round": round_number,
            "query": query,
        }

        summary = generate_final_answer(user_question, results)
        reflection = generate_reflection(query, summary)
        step["reflection"] = reflection

        search_steps.append(step)

        if not reflection.get("needs_more_search"):
            break

        query = reflection.get("next_query", query)

    final_results = remove_duplicate_sources(all_results)
    answer = generate_final_answer(user_question, final_results)

    return {
        "answer": answer,
        "results": final_results,
        "search_steps": search_steps,
    }
