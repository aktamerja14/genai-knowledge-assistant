from pathlib import Path
from langchain_community.document_loaders import TextLoader


def load_txt_file(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".txt":
        raise ValueError("Only TXT files are supported.")

    loader = TextLoader(
        str(path),
        encoding="utf-8"
    )

    documents = loader.load()

    return documents