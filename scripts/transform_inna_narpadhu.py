import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


RAW_PATH = (
    ROOT
    / "data"
    / "raw"
    / "inna_narpadhu"
    / "inna_narpadhu_raw.json"
)


OUTPUT_PATH = (
    ROOT
    / "data"
    / "literature"
    / "inna_narpadhu.json"
)


def transform():

    with open(RAW_PATH, "r", encoding="utf-8") as file:
        raw_data = json.load(file)


    print(f"Raw records found: {len(raw_data)}")


    transformed = []

    missing_poems = 0
    missing_explanations = 0


    for index, item in enumerate(raw_data, start=1):

        if not item.get("poem"):
            missing_poems += 1

        if not item.get("explanation"):
            missing_explanations += 1


        transformed.append({
            "id": index,
            "tamilText": item.get("poem", ""),
            "simpleTamilMeaning": item.get("explanation", ""),
            "englishMeaning": "",
            "transliteration": "",
            "keywords": [],
            "moral": "",
            "difficulty": "intermediate",
            "quiz": []
        })


    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:

        json.dump(
            transformed,
            file,
            ensure_ascii=False,
            indent=4
        )


    print("\n========== Transformation Report ==========")
    print(f"Total records processed : {len(transformed)}")
    print(f"Missing Poems           : {missing_poems}")
    print(f"Missing Explanations    : {missing_explanations}")

    print("\nTransformation Complete ✓")
    print(f"Dataset saved at:\n{OUTPUT_PATH}")


if __name__ == "__main__":
    transform()