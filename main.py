
from app.chains.json_parser_chain import get_json_parser_chain


def main():
    print("Starting JSON output parser...")

    chain = get_json_parser_chain()

    result = chain.invoke({
        "topic": "Retrieval-Augmented Generation (RAG)",
        "format_instructions": (
            "Return valid JSON only. Do not use Markdown code fences."
        )
    })

    print("\n--- JSON Output ---")
    print(result)

    print("\n--- Python Data Type ---")
    print(type(result))


if __name__ == "__main__":
    main()
