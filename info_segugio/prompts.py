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
