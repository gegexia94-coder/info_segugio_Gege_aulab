# Qui teniamo i prompt del progetto.
# Li separo dal file principale per non mischiare logica e testi lunghi.

def build_search_query_prompt(user_question: str) -> str:
    return f"""
Trasforma la domanda dell'utente in una query breve e precisa per una ricerca web.

Domanda utente:
{user_question}

Regole:
- usa parole semplici
- non inventare informazioni
- mantieni il senso della domanda
- restituisci solo la query finale
"""

def build_final_answer_prompt(user_question: str, results: list[dict]) -> str:
    sources_text = ""

    for index, item in enumerate(results, start=1):
        sources_text += f"""
Fonte {index}
Titolo: {item.get("title")}
URL: {item.get("url")}
Testo: {item.get("content")}
"""

    return f"""
Rispondi alla domanda dell'utente usando solo le fonti sotto.

Domanda:
{user_question}

Fonti:
{sources_text}

Regole:
- rispondi in italiano semplice
- non inventare informazioni
- se le fonti non bastano, dillo chiaramente
- chiudi con una breve lista delle fonti usate
"""
