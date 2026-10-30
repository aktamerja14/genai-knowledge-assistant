from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from app.model import get_model
from app.schemas import TopicExplanation


def get_pydantic_parser_chain():
    model = get_model()

    # Create Pydantic parser
    parser = PydanticOutputParser(
        pydantic_object=TopicExplanation
    )

    # Create prompt template
    prompt = ChatPromptTemplate.from_template(
        """
        Explain the following topic: {topic}

        Follow these formatting instructions:
        {format_instructions}
        """
    ).partial(
        format_instructions=parser.get_format_instructions()
    )

    # Connect prompt -> model -> parser
    chain = prompt | model | parser

    return chain