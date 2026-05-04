def transform_csv(csv_docs):
    transformed = []

    for item in csv_docs:
        content = item["content"]

        if len(content.strip()) < 20:
            continue

        transformed.append({
            "content": content,
            "type": "csv",
            "department": item["department"],
            "source": item["source"],
            "section": "row_data"
        })

    return transformed