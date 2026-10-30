
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

from app.model import get_model


def get_conditional_chain():
    model = get_model()

    positive_prompt = ChatPromptTemplate.from_template(
        "Write a polite thank-you response to this positive review: {review}"
    )

    negative_prompt = ChatPromptTemplate.from_template(
        "Write an empathetic apology for this negative review: {review}. "
        "Suggest contacting customer support."
    )

    positive_chain = positive_prompt | model | StrOutputParser()
    negative_chain = negative_prompt | model | StrOutputParser()

    branch = RunnableBranch(
        (
            lambda inputs: inputs["sentiment"] == "positive",
            positive_chain,
        ),
        negative_chain,
    )

    return branch
