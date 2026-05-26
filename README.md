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
