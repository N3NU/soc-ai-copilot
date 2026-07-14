import os
import re
from app.retrieval.vector_store import db

from app.config import (
    DOCS_PATH,
    META_KEYS
)



# REMOVE METADATA FROM DOC BEFORE CHUNKING


def remove_metadata_block(text):

    lines = text.split("\n")
#    print(lines)
    cleaned = []

    for line in lines:
        if any(line.startswith(key + ":") for key in META_KEYS):
            continue
        cleaned.append(line)

#    print(cleaned)
#    print("\n".join(cleaned))
    return "\n".join(cleaned)


# PARSE METADATA HEADER


def extract_metadata(text):

    metadata = {}

    for key in META_KEYS:
        pattern = rf"{key}:\s*(.*)"
        match = re.search(pattern, text)
        if match:
            metadata[key.lower()] = match.group(1).strip()
#    print(f"metadata:\n\n{metadata}")
    return metadata


# SECTION SPLITTING


def split_sections(text, metadata):
#    print(text)
    sections = re.split(r"\n(?=[A-Z_]+:)", text)
#    print(f"sections:\n{sections}\n\n\n")
    chunks = []

    for s in sections:
        s = s.strip()
        if not s:
            continue
        match = re.match(r"([A-Z_]+):", s)

        section = None

        if match:
            section = match.group(1).lower()

        chunk_metadata = metadata.copy()

        if section:
            chunk_metadata["section"] = section

        chunks.append(
            (s, chunk_metadata)
        )

    return chunks


# LOAD FILES RECURSIVELY


def load_docs():

    docs = []

    for root, _, files in os.walk(DOCS_PATH):
        for file in files:

            if not file.endswith(".txt"):
                continue

            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            metadata = extract_metadata(text)
            metadata["source"] = file
            clean_text = remove_metadata_block(text)
            chunks = split_sections(clean_text, metadata)

            docs.extend(chunks)

#    print(f"{docs}")
    return docs


# INGEST INTO CHROMA


def ingest():

    docs = load_docs()

    texts = []
    metas = []

    for chunk, meta in docs:
        texts.append(chunk)
        metas.append(meta)
#    print(f"\n\nTEXTS:\n\n\n{texts}\n\n")
#    print(f"METAS:\n\n\n{metas}")
    db.add_texts(
        texts=texts,
        metadatas=metas
    )

    print(f"Ingested {len(texts)} chunks into vector DB")


if __name__ == "__main__":
    ingest()