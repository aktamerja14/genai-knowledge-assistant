
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.model import get_model


def get_sequential_chain():
    model = get_model()

    explanation_prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in simple English in 2 sentences."
    )

    summary_prompt = ChatPromptTemplate.from_template(
        "Summarize this explanation in exactly 3 bullet points:\n\n"
        "{explanation}"
    )

    explanation_chain = explanation_prompt | model | StrOutputParser()
    summary_chain = summary_prompt | model | StrOutputParser()

    def run_sequential(inputs):
        print("Step 1: Generating explanation...")

        explanation = explanation_chain.invoke(inputs)

        if not explanation.strip():
            raise ValueError("The model returned an empty explanation.")

        print("Step 2: Explanation received.")
        print(explanation)

        print("Step 3: Generating summary...")

        summary = summary_chain.invoke({
            "explanation": explanation
        })

        if not summary.strip():
            raise ValueError("The model returned an empty summary.")

        return summary

    return run_sequential
