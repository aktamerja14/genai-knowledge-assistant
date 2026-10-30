from app.loaders.txt_loader import load_txt_file


def main():
    documents = load_txt_file(
        "data/sample_docs/rag_notes.txt"
    )

    print("\n--- Loaded Documents ---")
    print("Total documents:", len(documents))

    for index, document in enumerate(documents, start=1):
        print(f"\nDocument {index}")
        print("Content:")
        print(document.page_content)

        print("\nMetadata:")
        print(document.metadata)


if __name__ == "__main__":
    main()