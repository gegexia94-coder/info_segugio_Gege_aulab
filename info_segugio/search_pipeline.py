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


def run_search_flow(user_question: str, max_rounds: int = 2) -> dict:
    first_query = generate_search_query(user_question)

    all_results = []
    search_steps = []

    first_results = search_web(first_query, max_results=3)
    all_results.extend(first_results)

    search_steps.append({
        "round": 1,
        "query": first_query,
        "results_count": len(first_results),
    })

    reflection = generate_reflection(user_question, all_results)

    second_query = reflection.get("next_query") or f"{user_question} approfondimento informazioni aggiornate"
    second_results = search_web(second_query, max_results=3)
    all_results.extend(second_results)

    search_steps.append({
        "round": 2,
        "query": second_query,
        "results_count": len(second_results),
        "reflection": reflection,
    })

    final_results = remove_duplicate_sources(all_results)
    final_answer = generate_final_answer(user_question, final_results)

    return {
        "question": user_question,
        "results": final_results,
        "answer": final_answer,
        "search_steps": search_steps,
    }
