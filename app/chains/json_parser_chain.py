
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from app.model import get_model


def get_json_parser_chain():
    model = get_model()

    parser = JsonOutputParser()

    prompt = ChatPromptTemplate.from_template(
        """
        Explain the topic: {topic}

        Return a JSON object with these fields:
        - topic: topic name
        - definition: short definition
        - key_points: list of exactly 3 key points

        {format_instructions}
        """
    )

    chain = prompt | model | parser

    return chain
