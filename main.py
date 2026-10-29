
from app.chains.sequential_chain import get_sequential_chain


def main():
    print("Starting sequential chain...")

    chain = get_sequential_chain()

    result = chain({
        "topic": "Retrieval-Augmented Generation (RAG)"
    })

    print("\nFinal summary:")
    print(result)


if __name__ == "__main__":
    main()
