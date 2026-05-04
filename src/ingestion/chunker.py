from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter


def chunk_markdown(md_docs):
    headers_to_split_on = [
        ("#", "h1"),
        ("##", "h2"),
        ("###", "h3"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on
    )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ". ", " "]
    )

    chunked_docs = []

    for doc in md_docs:
        splits = markdown_splitter.split_text(doc["content"])

        for split in splits:
            section_text = split.page_content
            metadata = split.metadata

            section = (
                metadata.get("h3")
                or metadata.get("h2")
                or metadata.get("h1")
                or "unknown"
            )

            sub_chunks = text_splitter.split_text(section_text)

            for chunk in sub_chunks:
                if len(chunk.strip()) < 30:
                    continue

                chunked_docs.append({
                    "content": chunk,
                    "type": "markdown",
                    "department": doc["department"],
                    "source": doc["source"],
                    "section": section
                })

    return chunked_docs