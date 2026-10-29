
from app.chains.parallel_chain import get_parallel_chain


def main():
    print("Starting parallel chain...")

    chain = get_parallel_chain()

    result = chain.invoke({
        "topic": "Retrieval-Augmented Generation (RAG)"
    })

    print("\n--- Explanation ---")
    print(result["explanation"])

    print("\n--- Key Points ---")
    print(result["key_points"])


if __name__ == "__main__":
    main()
