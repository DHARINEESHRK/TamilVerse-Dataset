import json
from pathlib import Path


# ==============================
# Paths
# ==============================

ROOT = Path(__file__).parent.parent

RAW_PATH = (
    ROOT
    / "data"
    / "raw"
    / "pazhamozhi"
    / "pazhamozhi_raw.json"
)

OUTPUT_PATH = (
    ROOT
    / "data"
    / "literature"
    / "pazhamozhi.json"
)


# ==============================
# Load Raw Dataset
# ==============================

def load_raw_data():
    with open(
        RAW_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


# ==============================
# Transform Dataset
# ==============================

def transform():

    raw_records = load_raw_data()

    print(f"Raw records found: {len(raw_records)}")

    dataset = []

    missing_title = 0
    missing_verse = 0
    missing_explanation = 0
    missing_moral = 0


    for item in raw_records:

        # Data Quality Checks

        if not item.get("blue_topic"):
            missing_title += 1

        if not item.get("verse"):
            missing_verse += 1

        if not item.get("explanation"):
            missing_explanation += 1

        if not item.get("karuthurai"):
            missing_moral += 1


        # TamilVerse Schema Mapping

        record = {

            "id": item["id"],

            "title": item.get(
                "blue_topic",
                ""
            ),

            "tamilText": item.get(
                "verse",
                ""
            ),

            "simpleTamilMeaning": item.get(
                "explanation",
                ""
            ),

            "moral": item.get(
                "karuthurai",
                ""
            ),


            # AI Enrichment Fields

            "englishMeaning": "",

            "transliteration": "",

            "keywords": [],

            "difficulty": "intermediate",

            "quiz": []
        }

        dataset.append(record)


    # Create folder if missing

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    # Save transformed dataset

    with open(
        OUTPUT_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            dataset,
            file,
            ensure_ascii=False,
            indent=4
        )


    # Transformation Report

    print("\n========== Transformation Report ==========")

    print(
        f"Total records processed : {len(dataset)}"
    )

    print("\nMissing Fields")

    print(
        f"Missing Topics          : {missing_title}"
    )

    print(
        f"Missing Verses          : {missing_verse}"
    )

    print(
        f"Missing Explanations    : {missing_explanation}"
    )

    print(
        f"Missing Morals          : {missing_moral}"
    )

    print("\nTransformation Complete ✓")

    print(
        f"Dataset saved at:\n{OUTPUT_PATH}"
    )


# ==============================
# Main
# ==============================

if __name__ == "__main__":
    transform()