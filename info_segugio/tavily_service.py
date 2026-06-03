from tavily import TavilyClient

from info_segugio.config import Config

client = TavilyClient(api_key=Config.TAVILY_API_KEY)


def search_web(query: str, max_results: int = 5) -> list[dict]:
    response = client.search(
        query=query,
        max_results=max_results,
    )

    return response.get("results", [])
