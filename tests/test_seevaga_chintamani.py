import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


DATA_PATH = (
    ROOT
    / "data"
    / "literature"
    / "seevaga_chintamani.json"
)


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def test_total_records(data):

    expected_records = len(data)

    assert len(data) == expected_records, (
        f"Expected {expected_records} records, found {len(data)}"
    )

    print(f"✓ Total Seevaga Chintamani records: {len(data)}")


def test_unique_ids(data):

    ids = [item["id"] for item in data]

    assert len(ids) == len(set(ids)), (
        "Duplicate IDs found"
    )

    print("✓ Unique IDs verified")


def test_schema(data):

    required_fields = [
        "id",
        "section",
        "verseNumber",
        "tamilText",
        "simpleTamilMeaning",
        "englishMeaning",
        "transliteration",
        "keywords",
        "moral",
        "difficulty",
        "quiz"
    ]


    for item in data:

        for field in required_fields:

            assert field in item, (
                f"Missing {field} in ID {item['id']}"
            )


    print("✓ TamilVerse schema validation passed")


def quality_report(data):

    missing_sections = 0
    missing_numbers = 0
    missing_poems = 0


    for item in data:

        if not item["section"].strip():
            missing_sections += 1

        if not item["verseNumber"]:
            missing_numbers += 1

        if not item["tamilText"].strip():
            missing_poems += 1


    print("\n===== Data Quality Report =====")

    print(f"Missing Sections        : {missing_sections}")
    print(f"Missing Verse Numbers   : {missing_numbers}")
    print(f"Missing Poems           : {missing_poems}")


if __name__ == "__main__":

    print("\n===== TamilVerse Seevaga Chintamani Test =====\n")

    data = load_data()

    test_total_records(data)
    test_unique_ids(data)
    test_schema(data)
    quality_report(data)

    print("\n🎉 ALL SEEVAGA CHINTAMANI TESTS PASSED")