
from app.model import get_model


def main():
    model = get_model()

    response = model.invoke(
        "Explain Generative AI in 3 simple sentences."
    )

    print(response.content)


if __name__ == "__main__":
    main()
