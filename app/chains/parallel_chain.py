
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

from app.model import get_model


def invoke_with_retry(chain, inputs, name, max_attempts=3):
    """Retry when a model returns empty text."""
    for attempt in range(1, max_attempts + 1):
        result = chain.invoke(inputs)

        if isinstance(result, str) and result.strip():
            return result.strip()

        print(
            f"{name}: empty response "
            f"(attempt {attempt}/{max_attempts})"
        )

    raise RuntimeError(
        f"{name} returned no text after {max_attempts} attempts."
    )


def get_parallel_chain():
    model = get_model()

    explanation_prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in simple English in at most 100 words. "
        "Include one short example."
    )

    key_points_prompt = ChatPromptTemplate.from_template(
        "Give exactly 3 short bullet points about {topic}. "
        "Use at most 20 words per bullet."
    )

    explanation_chain = explanation_prompt | model | StrOutputParser()
    key_points_chain = key_points_prompt | model | StrOutputParser()

    return RunnableParallel(
        explanation=RunnableLambda(
            lambda inputs: invoke_with_retry(
                explanation_chain, inputs, "Explanation"
            )
        ),
        key_points=RunnableLambda(
            lambda inputs: invoke_with_retry(
                key_points_chain, inputs, "Key points"
            )
        ),
    )
