import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


RAW_PATH = (
    ROOT
    / "data"
    / "raw"
    / "seevaga_chintamani"
    / "seevaga_chintamani_raw.json"
)


OUTPUT_PATH = (
    ROOT
    / "data"
    / "literature"
    / "seevaga_chintamani.json"
)


def transform():

    with open(RAW_PATH, "r", encoding="utf-8") as file:
        raw_data = json.load(file)


    transformed = []

    missing_sections = 0
    missing_numbers = 0
    missing_poems = 0


    for section in raw_data:

        section_name = section.get("title", "")

        if not section_name:
            missing_sections += 1


        for poem in section.get("poems", []):

            if not poem.get("number"):
                missing_numbers += 1


            if not poem.get("poem"):
                missing_poems += 1


            transformed.append({
                "id": len(transformed) + 1,
                "section": section_name,
                "verseNumber": poem.get("number", ""),
                "tamilText": poem.get("poem", ""),
                "simpleTamilMeaning": "",
                "englishMeaning": "",
                "transliteration": "",
                "keywords": [],
                "moral": "",
                "difficulty": "advanced",
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

    print(f"Total records processed : {len(transformed)}")

    print("\nMissing Fields")

    print(f"Missing Sections        : {missing_sections}")
    print(f"Missing Verse Numbers   : {missing_numbers}")
    print(f"Missing Poems           : {missing_poems}")


    print("\nTransformation Complete ✓")
    print(f"Dataset saved at:\n{OUTPUT_PATH}")


if __name__ == "__main__":
    transform()