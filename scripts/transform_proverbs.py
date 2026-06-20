import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


RAW_PATH = (
    ROOT
    / "data"
    / "raw"
    / "proverbs"
    / "proverbs_raw.json"
)


OUTPUT_PATH = (
    ROOT
    / "data"
    / "proverbs"
    / "tamil_proverbs.json"
)


def transform():

    print("Loading Tamil Proverbs dataset...")

    with open(
        RAW_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        raw_data = json.load(file)


    print(f"Raw records found: {len(raw_data)}")


    transformed = []


    missing_proverbs = 0
    missing_english = 0


    for item in raw_data:

        proverb = str(
            item.get("Tamil", "")
        ).strip()

        english = str(
            item.get("English", "")
        ).strip()


        if not proverb:
            missing_proverbs += 1


        if not english:
            missing_english += 1


        transformed.append({
            "id": len(transformed) + 1,
            "proverb": proverb,
            "transliteration": "",
            "simpleTamilMeaning": "",
            "englishMeaning": english,
            "moral": "",
            "category": "",
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
        f"Total Proverbs Processed : {len(transformed)}"
    )

    print("\nMissing Fields")

    print(
        f"Missing Proverbs         : {missing_proverbs}"
    )

    print(
        f"Missing English Meaning  : {missing_english}"
    )


    print("\nTransformation Complete ✓")
    print(
        f"Dataset saved at:\n{OUTPUT_PATH}"
    )


if __name__ == "__main__":
    transform()