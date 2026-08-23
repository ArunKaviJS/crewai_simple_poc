import os
import pandas as pd


DATA_DIRECTORY = "data"


def list_datasets():

    print("\n🔧 DATA TOOL: list_datasets()")

    if not os.path.exists(DATA_DIRECTORY):
        return []

    datasets = []

    for filename in os.listdir(DATA_DIRECTORY):

        if filename.endswith(".csv"):

            datasets.append(filename)

    return datasets


def inspect_dataset(filename):

    print(
        f"\n🔧 DATA TOOL: "
        f"inspect_dataset('{filename}')"
    )

    path = os.path.join(
        DATA_DIRECTORY,
        filename
    )

    if not os.path.exists(path):

        return {
            "error": f"{filename} not found."
        }

    try:

        df = pd.read_csv(path)

        result = {
            "filename": filename,
            "rows": len(df),
            "columns": list(df.columns),
            "data_types": {
                col: str(dtype)
                for col, dtype
                in df.dtypes.items()
            },
            "sample": df.head(5).to_dict(
                orient="records"
            )
        }

        return result

    except Exception as e:

        return {
            "error": str(e)
        }


def analyze_dataset(
    filename,
    analysis
):

    print(
        f"\n🔧 DATA TOOL: "
        f"analyze_dataset("
        f"'{filename}', "
        f"'{analysis}')"
    )

    path = os.path.join(
        DATA_DIRECTORY,
        filename
    )

    if not os.path.exists(path):

        return {
            "error": f"{filename} not found."
        }

    try:

        df = pd.read_csv(path)

        numeric_columns = (
            df.select_dtypes(
                include="number"
            ).columns.tolist()
        )

        result = {
            "filename": filename,
            "requested_analysis": analysis,
            "rows": len(df),
            "columns": list(df.columns),
            "numeric_columns": numeric_columns,
        }

        # Basic statistics
        result["statistics"] = (
            df[numeric_columns]
            .describe()
            .to_dict()
            if numeric_columns
            else {}
        )

        return result

    except Exception as e:

        return {
            "error": str(e)
        }