
import os

from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()


def get_model():
    api_key = os.getenv("LLM_API_KEY")
    model_name = os.getenv("LLM_MODEL", "openrouter/free")

    if not api_key:
        raise ValueError("LLM_API_KEY is missing from .env")

    model = ChatOpenRouter(
        model=model_name,
        api_key=api_key,
        temperature=0,
        max_tokens=300,
    )

    return model
