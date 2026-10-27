
from langchain_core.prompts import ChatPromptTemplate


def get_basic_prompt():
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a Generative AI teacher. "
            "Explain concepts in easy English with examples."
        ),
        (
            "human",
            "Explain this concept: {topic}"
        ),
    ])

    return prompt
