
from langchain_openrouter import ChatOpenRouter

from app.config import get_llm_config


def get_model():
    config = get_llm_config()

    if config["provider"] != "openrouter":
        raise ValueError("Unsupported LLM provider")

    return ChatOpenRouter(
        model=config["model"],
        api_key=config["api_key"],
        temperature=0,
        max_tokens=600,
        reasoning={"effort": "none"},
    )
