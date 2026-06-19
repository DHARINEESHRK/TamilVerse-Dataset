import json
from pathlib import Path


ROOT = Path(__file__).parent.parent

RAW_PATH = (
    ROOT
    / "data"
    / "raw"
    / "konraiventhan"
    / "konraiventhan_raw.json"
)

OUTPUT_PATH = (
    ROOT
    / "data"
    / "literature"
    / "konraiventhan.json"
)


def transform():

    with open(RAW_PATH, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    print(f"Raw records found: {len(raw_data)}")

    transformed = []

    missing_section = 0
    missing_poem = 0
    missing_explanation = 0

    for index, item in enumerate(raw_data, start=1):

        if not item.get("Section"):
            missing_section += 1

        if not item.get("Poem Line"):
            missing_poem += 1

        if not item.get("Explanation"):
            missing_explanation += 1


        transformed.append({
            "id": index,
            "title": item.get("Section", ""),
            "tamilText": item.get("Poem Line", ""),
            "simpleTamilMeaning": item.get("Explanation", ""),
            "englishMeaning": "",
            "transliteration": "",
            "keywords": [],
            "moral": "",
            "difficulty": "beginner",
            "quiz": []
        })


    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        json.dump(
            transformed,
            file,
            ensure_ascii=False,
            indent=4
        )


    print("\n========== Transformation Report ==========")
    print(f"Total records processed : {len(transformed)}")
    print(f"Missing Sections        : {missing_section}")
    print(f"Missing Poems           : {missing_poem}")
    print(f"Missing Explanations    : {missing_explanation}")

    print("\nTransformation Complete ✓")
    print(f"Dataset saved at:\n{OUTPUT_PATH}")


if __name__ == "__main__":
    transform()