def build_search_query_prompt(user_question: str) -> str:
    return f"""
Trasforma questa domanda in una query breve e precisa per ricerca web.

Domanda utente:
{user_question}

Rispondi solo con la query.
"""

def build_final_answer_prompt(user_question: str, results: list[dict]) -> str:
    sources_text = ""

    for index, item in enumerate(results, start=1):
        title = item.get("title", "Titolo non disponibile")
        content = item.get("content", "")
        url = item.get("url", "")
        sources_text += f"\nFonte {index}: {title}\nURL: {url}\nContenuto: {content}\n"

    return f"""
Rispondi alla domanda usando solo le fonti raccolte.

Domanda:
{user_question}

Fonti:
{sources_text}

Scrivi una risposta chiara, sintetica e verificabile.
"""

def build_reflection_prompt(query: str, summary: str) -> str:
    return f"""
Sei un assistente di web research.

Devi valutare se serve una nuova ricerca web per migliorare la risposta.

Query usata:
{query}

Riassunto attuale:
{summary}

Rispondi SOLO con JSON valido.
Non scrivere markdown.
Non scrivere spiegazioni fuori dal JSON.

Formato obbligatorio:
{{
  "needs_more_search": true,
  "reason": "spiega in 1 frase cosa manca",
  "next_query": "scrivi una nuova query precisa e diversa"
}}
"""
