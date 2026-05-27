# Info Segugio

Questo progetto è un assistente AI per fare ricerche web guidate.

## Obiettivo

L'utente scrive una domanda.
Il sistema prova a trasformarla in una query migliore.
Poi cerca informazioni online e prepara una risposta riassunta.

## Librerie usate

- Chainlit: crea la chat nel browser
- OpenAI: aiuta a migliorare query e riassunti
- Tavily: fa la ricerca web
- python-dotenv: legge le chiavi dal file .env

## Nota sicurezza

Le chiavi API non devono stare nel codice.
Devono stare solo nel file .env.

## Avanzamento 01 - Configurazione

In questo step ho aggiunto il file `config.py`.

Questo file serve per leggere le chiavi API dal file `.env`, senza scriverle direttamente nel codice.

Variabili usate:

- OPENAI_API_KEY: chiave per usare OpenAI
- TAVILY_API_KEY: chiave per usare Tavily
- OPENAI_MODEL: modello OpenAI scelto per il progetto

Ho fatto anche un test da terminale per verificare che le chiavi siano presenti, senza stamparle.

## Avanzamento 02 - Prompt per query di ricerca

In questo step ho creato il file `prompts.py`.

Questo file contiene una funzione che costruisce il prompt per trasformare la domanda dell'utente in una query più adatta alla ricerca web.

Per ora non chiamo ancora OpenAI.
Prima controllo solo che il prompt venga costruito bene.

## Avanzamento 03 - OpenAI per creare query

In questo step ho creato il file `openai_service.py`.

Questo file usa OpenAI per trasformare una domanda normale in una query più utile per la ricerca web.

Per ora non uso ancora Tavily.
Sto testando solo se OpenAI risponde con una query breve.

## Avanzamento 04 - Ricerca web con Tavily

In questo step ho creato il file `tavily_service.py`.

Questo file usa Tavily per fare una ricerca web partendo da una query.

Per ora Tavily viene testato da solo.
Nel prossimo step unirò OpenAI e Tavily nello stesso flusso.

## Avanzamento 05 - Pipeline OpenAI + Tavily

In questo step ho creato `search_pipeline.py`.

Questo file collega due parti:
- OpenAI, che trasforma la domanda in una query
- Tavily, che usa quella query per cercare online

Per ora il flusso viene testato solo da terminale.
Nel prossimo step lo collegherò alla chat Chainlit.
