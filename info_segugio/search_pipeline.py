from info_segugio.openai_service import (
    generate_search_query,
    generate_reflection,
    generate_final_answer,
)
from info_segugio.tavily_service import search_web


MIN_SEARCH_ROUNDS = 4
MAX_SEARCH_ROUNDS = 5
RESULTS_PER_SEARCH = 5


def remove_duplicate_sources(results: list[dict]) -> list[dict]:
    seen_urls = set()
    unique_results = []

    for item in results:
        url = item.get("url")
        if url and url not in seen_urls:
            seen_urls.add(url)
            unique_results.append(item)

    return unique_results


def build_fallback_query(user_question: str, round_number: int) -> str:
    return (
        f"{user_question} approfondimento fonti dettagli "
        f"analisi contesto ricerca {round_number}"
    )


def run_search_flow(user_question: str) -> dict:
    search_steps = []
    all_results = []

    query = generate_search_query(user_question)

    for round_number in range(1, MAX_SEARCH_ROUNDS + 1):
        results = search_web(query, max_results=RESULTS_PER_SEARCH)
        all_results.extend(results)

        partial_results = remove_duplicate_sources(all_results)
        summary = generate_final_answer(user_question, partial_results)
        reflection = generate_reflection(query, summary)

        search_steps.append({
            "round": round_number,
            "query": query,
            "reflection": reflection,
            "results_found": len(results),
        })

        if round_number >= MIN_SEARCH_ROUNDS and not reflection.get("needs_more_search"):
            break

        query = reflection.get("next_query") or build_fallback_query(
            user_question,
            round_number + 1,
        )

    final_results = remove_duplicate_sources(all_results)
    answer = generate_final_answer(user_question, final_results)

    return {
        "answer": answer,
        "results": final_results,
        "search_steps": search_steps,
    }
