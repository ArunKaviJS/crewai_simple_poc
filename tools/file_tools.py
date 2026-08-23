# tools/file_tools.py


def list_files():
    """
    Return all available files.
    """

    print("\n🔧 TOOL CALLED: list_files()")

    files = [
        "report.pdf",
        "invoice.xlsx",
        "customer.csv",
        "project.docx",
        "sales_report.pdf"
    ]

    return files


def search_file(filename):
    """
    Search for a particular file.
    """

    print(f"\n🔧 TOOL CALLED: search_file(filename='{filename}')")

    files = [
        "report.pdf",
        "invoice.xlsx",
        "customer.csv",
        "project.docx",
        "sales_report.pdf"
    ]

    matches = [
        file for file in files
        if filename.lower() in file.lower()
    ]

    if matches:
        return {
            "found": True,
            "files": matches
        }

    return {
        "found": False,
        "files": []
    }