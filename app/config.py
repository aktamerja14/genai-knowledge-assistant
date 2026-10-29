
import os

from dotenv import load_dotenv

load_dotenv()


def get_required_env(name: str) -> str:
    """Return a required environment variable or raise a safe error."""
    value = os.getenv(name)

    if not value or not value.strip():
        raise RuntimeError(
            f"Required configuration is missing: {name}"
        )

    return value.strip()


def get_llm_config() -> dict[str, str]:
    """Load validated LLM configuration."""
    return {
        "provider": get_required_env("LLM_PROVIDER"),
        "model": get_required_env("LLM_MODEL"),
        "api_key": get_required_env("LLM_API_KEY"),
    }
