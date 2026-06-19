import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


RAW_PATH = (
    ROOT
    / "data"
    / "raw"
    / "acharakovai"
    / "acharakovai_raw.json"
)

OUTPUT_PATH = (
    ROOT
    / "data"
    / "literature"
    / "acharakovai.json"
)


def transform():

    with open(RAW_PATH, "r", encoding="utf-8") as file:
        raw_data = json.load(file)


    print(f"Raw records found: {len(raw_data)}")


    transformed = []

    missing_number = 0
    missing_topic = 0
    missing_poem_type = 0
    missing_poem = 0
    missing_explanation = 0
    missing_moral = 0


    for item in raw_data:

        if not item.get("number"):
            missing_number += 1

        if not item.get("topic"):
            missing_topic += 1

        if not item.get("venbha"):
            missing_poem_type += 1

        if not item.get("poem"):
            missing_poem += 1

        if not item.get("explanation"):
            missing_explanation += 1

        if not item.get("karuthurai"):
            missing_moral += 1


        transformed.append({
            "id": int(item.get("number", 0)),
            "poemNumber": item.get("number", ""),
            "title": item.get("topic", ""),
            "poemType": item.get("venbha", ""),
            "tamilText": item.get("poem", ""),
            "simpleTamilMeaning": item.get("explanation", ""),
            "moral": item.get("karuthurai", ""),
            "englishMeaning": "",
            "transliteration": "",
            "keywords": [],
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

    print("\nMissing Fields")

    print(f"Missing Numbers         : {missing_number}")
    print(f"Missing Topics          : {missing_topic}")
    print(f"Missing Poem Types      : {missing_poem_type}")
    print(f"Missing Poems           : {missing_poem}")
    print(f"Missing Explanations    : {missing_explanation}")
    print(f"Missing Morals          : {missing_moral}")

    print("\nTransformation Complete ✓")
    print(f"Dataset saved at:\n{OUTPUT_PATH}")


if __name__ == "__main__":
    transform()