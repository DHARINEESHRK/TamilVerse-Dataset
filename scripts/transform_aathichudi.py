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
    / "aathichudi"
    / "aathichudi.json"
)

OUTPUT_PATH = (
    ROOT
    / "data"
    / "literature"
    / "aathichudi.json"
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
        data = json.load(file)

    return data["athisudi"]


# ==============================
# Transform Dataset
# ==============================

def transform():

    raw_records = load_raw_data()

    print(f"Raw records found: {len(raw_records)}")

    dataset = []

    missing_meaning = 0
    missing_paraphrase = 0
    missing_translation = 0


    for item in raw_records:

        # Data quality checks
        if not item.get("meaning"):
            missing_meaning += 1
            print(
                f"WARNING: Missing meaning in record {item['number']}"
            )

        if not item.get("paraphrase"):
            missing_paraphrase += 1
            print(
                f"WARNING: Missing paraphrase in record {item['number']}"
            )

        if not item.get("translation"):
            missing_translation += 1
            print(
                f"WARNING: Missing translation in record {item['number']}"
            )


        # Convert to TamilVerse schema
        record = {

            "id": item["number"],

            "tamilText": item["poem"],


            # Existing educational data
            "wordMeaning": item.get(
                "meaning",
                ""
            ),

            "simpleTamilMeaning": item.get(
                "paraphrase",
                ""
            ),

            "englishMeaning": item.get(
                "translation",
                ""
            ),


            # Future AI enrichment fields
            "transliteration": "",

            "keywords": [],

            "moral": "",

            "difficulty": "beginner",

            "quiz": []
        }

        dataset.append(record)


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


    # Final report
    print("\n========== Transformation Report ==========")

    print(f"Total records processed : {len(dataset)}")
    print(f"Missing meanings        : {missing_meaning}")
    print(f"Missing paraphrases     : {missing_paraphrase}")
    print(f"Missing translations    : {missing_translation}")

    print("\nTransformation Complete ✓")
    print(f"Dataset saved at:\n{OUTPUT_PATH}")


# ==============================
# Main
# ==============================

if __name__ == "__main__":

    transform()