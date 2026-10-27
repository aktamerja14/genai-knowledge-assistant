
from app.model import get_model
from app.prompts.basic_prompt import get_basic_prompt


def main():
    model = get_model()
    prompt = get_basic_prompt()

    chain = prompt | model

    response = chain.invoke({
        "topic": "Embeddings in Generative AI"
    })

    print(response.content)


if __name__ == "__main__":
    main()
