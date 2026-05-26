import os
from dotenv import load_dotenv

# Carico le variabili dal file .env
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    OPENAI_MODEL = "gpt-4o-mini"
