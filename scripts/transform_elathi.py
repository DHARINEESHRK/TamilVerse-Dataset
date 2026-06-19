import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


RAW_PATH = (
    ROOT
    / "data"
    / "raw"
    / "elathi"
    / "elathi_raw.json"
)


OUTPUT_PATH = (
    ROOT
    / "data"
    / "literature"
    / "elathi.json"
)


def transform():

    with open(RAW_PATH, "r", encoding="utf-8") as file:
        raw_data = json.load(file)


    print(f"Raw records found: {len(raw_data)}")


    transformed = []

    missing_title = 0
    missing_verse = 0
    missing_explanation = 0
    missing_moral = 0


    for item in raw_data:

        if not item.get("blue_topic"):
            missing_title += 1

        if not item.get("verse"):
            missing_verse += 1

        if not item.get("explanation"):
            missing_explanation += 1

        if not item.get("karuthurai"):
            missing_moral += 1


        transformed.append({

            "id": item["id"],

            "title": item.get(
                "blue_topic",
                ""
            ),

            "verseNumber": item.get(
                "verse_number",
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
        f"Total records processed : {len(transformed)}"
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


if __name__ == "__main__":
    transform()