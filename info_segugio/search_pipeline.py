from info_segugio.openai_service import generate_search_query
from info_segugio.tavily_service import search_web

# Questo file coordina i pezzi già creati.
# Prima migliora la domanda, poi cerca sul web.

def run_search_flow(user_question: str) -> dict:
    search_query = generate_search_query(user_question)
    results = search_web(search_query, max_results=3)
    return {"question": user_question, "query": search_query, "results": results}
