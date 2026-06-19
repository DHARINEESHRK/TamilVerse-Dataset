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
    / "naaladiyar"
    / "naaladiyar_raw.json"
)

OUTPUT_PATH = (
    ROOT
    / "data"
    / "literature"
    / "naaladiyar.json"
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

    missing_topic = 0
    missing_poem = 0
    missing_explanation = 0
    missing_paal = 0
    missing_iyal = 0


    for index, item in enumerate(raw_records, start=1):

        # Data Quality Checks

        if not item.get("topic"):
            missing_topic += 1
            print(f"WARNING: Missing topic in record {index}")

        if not item.get("poem"):
            missing_poem += 1
            print(f"WARNING: Missing poem in record {index}")

        if not item.get("explanation"):
            missing_explanation += 1
            print(f"WARNING: Missing explanation in record {index}")

        if not item.get("paal"):
            missing_paal += 1
            print(f"WARNING: Missing paal in record {index}")

        if not item.get("iyal"):
            missing_iyal += 1
            print(f"WARNING: Missing iyal in record {index}")


        # TamilVerse Schema Mapping

        record = {

            "id": index,

            "title": item.get(
                "topic",
                ""
            ),

            "tamilText": item.get(
                "poem",
                ""
            ),

            "simpleTamilMeaning": item.get(
                "explanation",
                ""
            ),

            "paal": item.get(
                "paal",
                ""
            ),

            "iyal": item.get(
                "iyal",
                ""
            ),


            # AI Enrichment Fields (Future)

            "englishMeaning": "",

            "transliteration": "",

            "keywords": [],

            "moral": "",

            "difficulty": "intermediate",

            "quiz": []
        }


        dataset.append(record)


    # Save Final Dataset

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
            dataset,
            file,
            ensure_ascii=False,
            indent=4
        )


    # Transformation Report

    print("\n========== Transformation Report ==========")

    print(f"Total records processed : {len(dataset)}")

    print("\nMissing Fields")

    print(f"Missing Topics          : {missing_topic}")
    print(f"Missing Poems           : {missing_poem}")
    print(f"Missing Explanations    : {missing_explanation}")
    print(f"Missing Paal            : {missing_paal}")
    print(f"Missing Iyal            : {missing_iyal}")

    print("\nTransformation Complete ✓")
    print(f"Dataset saved at:\n{OUTPUT_PATH}")


# ==============================
# Main
# ==============================

if __name__ == "__main__":
    transform()