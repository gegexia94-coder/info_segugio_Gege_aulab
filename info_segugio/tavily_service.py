from tavily import TavilyClient

from info_segugio.config import Config

# Questo client parla con Tavily.
# La chiave arriva dal file .env tramite Config.
client = TavilyClient(api_key=Config.TAVILY_API_KEY)

def search_web(query: str, max_results: int = 3) -> list[dict]:
    response = client.search(
        query=query,
        max_results=max_results,
        include_answer=False,
    )

    return response.get("results", [])
