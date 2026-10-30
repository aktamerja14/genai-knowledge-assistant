
from app.chains.conditional_chain import get_conditional_chain


def main():
    print("Starting conditional chain...")

    chain = get_conditional_chain()

    result = chain.invoke({
    "sentiment": "negative",
    "review": "The service was very poor and staff were unhelpful."
    })

    print("\n--- Generated Response ---")
    print(result)


if __name__ == "__main__":
    main()
