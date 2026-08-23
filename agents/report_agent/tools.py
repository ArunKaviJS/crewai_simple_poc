import os
from datetime import datetime


REPORT_DIRECTORY = "outputs/reports"


def save_report(
    filename,
    content
):

    print(
        f"\n🔧 REPORT TOOL: "
        f"save_report('{filename}')"
    )

    os.makedirs(
        REPORT_DIRECTORY,
        exist_ok=True
    )

    path = os.path.join(
        REPORT_DIRECTORY,
        filename
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)

    return {
        "success": True,
        "path": path,
        "created_at": datetime.now().isoformat()
    }