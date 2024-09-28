import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

class LLMWrapper():
    def __init__(self) -> None:
        load_dotenv(override=True)

    def get_llm(self) -> ChatOpenAI:
        return ChatOpenAI(model= os.environ.get("FINE_TUNING_MODEL"), 
                     api_key=os.environ.get("OPENAI_API_KEY"))

