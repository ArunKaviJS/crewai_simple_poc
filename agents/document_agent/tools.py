import os


DOCUMENT_DIRECTORY = "data/documents"


def list_documents():

    print("\n🔧 DOCUMENT TOOL: list_documents()")

    if not os.path.exists(DOCUMENT_DIRECTORY):
        return []

    files = []

    for filename in os.listdir(DOCUMENT_DIRECTORY):

        path = os.path.join(
            DOCUMENT_DIRECTORY,
            filename
        )

        if os.path.isfile(path):
            files.append(filename)

    return files


def read_document(filename):

    print(
        f"\n🔧 DOCUMENT TOOL: "
        f"read_document('{filename}')"
    )

    path = os.path.join(
        DOCUMENT_DIRECTORY,
        filename
    )

    if not os.path.exists(path):
        return {
            "error": f"Document '{filename}' not found."
        }

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

        return {
            "filename": filename,
            "content": content
        }

    except Exception as e:

        return {
            "error": str(e)
        }


def search_document(keyword):

    print(
        f"\n🔧 DOCUMENT TOOL: "
        f"search_document('{keyword}')"
    )

    documents = list_documents()

    results = []

    for filename in documents:

        path = os.path.join(
            DOCUMENT_DIRECTORY,
            filename
        )

        try:

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            if keyword.lower() in content.lower():

                results.append({
                    "filename": filename,
                    "match": True
                })

        except Exception:
            continue

    return results