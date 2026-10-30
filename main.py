from app.chains.pydantic_parser_chain import get_pydantic_parser_chain


def main():
    chain = get_pydantic_parser_chain()

    result = chain.invoke({
        "topic": "Retrieval-Augmented Generation (RAG)"
    })

    print("\n--- Pydantic Output ---")
    print(result)

    print("\n--- Individual Fields ---")
    print("Topic:", result.topic)
    print("Definition:", result.definition)
    print("Key Points:", result.key_points)

    print("\n--- Result Type ---")
    print(type(result))


if __name__ == "__main__":
    main()