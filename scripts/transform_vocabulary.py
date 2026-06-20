import json
import pandas as pd
from pathlib import Path


ROOT = Path(__file__).parent.parent


RAW_PATH = (
    ROOT
    / "data"
    / "raw"
    / "vocabulary"
    / "tamil_vocabulary_raw.xlsx"
)


OUTPUT_PATH = (
    ROOT
    / "data"
    / "vocabulary"
    / "tamil_vocabulary.json"
)


def transform():

    print("Loading vocabulary dataset...")

    # Read Excel without assuming a header row
    df = pd.read_excel(
        RAW_PATH,
        header=None
    )

    # Assign proper column names
    df.columns = [
        "No",
        "English",
        "Tamil",
        "Transliteration"
    ]

    print(f"Total rows found: {len(df)}")


    transformed = []

    current_category = "Unknown"

    missing_english = 0
    missing_tamil = 0
    missing_transliteration = 0


    for _, row in df.iterrows():

        english = str(row["English"]).strip()
        tamil = str(row["Tamil"]).strip()
        transliteration = str(
            row["Transliteration"]
        ).strip()


        # Detect category rows
        # Example:
        # BODY PARTS – உடல் உறுப்புகள் – UDAL URUPPUKAL
        if (
            "–" in english
            and tamil == "nan"
        ):
            current_category = (
                english
                .split("–")[0]
                .strip()
                .title()
            )
            continue


        # Skip completely empty rows
        if (
            english == "nan"
            and tamil == "nan"
        ):
            continue


        # Count missing fields
        if (
            english == "nan"
            or english == ""
        ):
            missing_english += 1


        if (
            tamil == "nan"
            or tamil == ""
        ):
            missing_tamil += 1


        if (
            transliteration == "nan"
            or transliteration == ""
        ):
            missing_transliteration += 1


        transformed.append({
            "id": len(transformed) + 1,

            "category": current_category,

            "englishWord": (
                ""
                if english == "nan"
                else english
            ),

            "tamilWord": (
                ""
                if tamil == "nan"
                else tamil
            ),

            "transliteration": (
                ""
                if transliteration == "nan"
                else transliteration
            ),

            "difficulty": "basic"
        })


    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    with open(
        OUTPUT_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            transformed,
            file,
            ensure_ascii=False,
            indent=4
        )


    print("\n========== Transformation Report ==========")

    print(
        f"Total vocabulary records : {len(transformed)}"
    )

    print("\nMissing Fields")

    print(
        f"Missing English Words      : {missing_english}"
    )

    print(
        f"Missing Tamil Words        : {missing_tamil}"
    )

    print(
        f"Missing Transliteration    : {missing_transliteration}"
    )

    print("\nTransformation Complete ✓")

    print(
        f"Dataset saved at:\n{OUTPUT_PATH}"
    )


if __name__ == "__main__":
    transform()