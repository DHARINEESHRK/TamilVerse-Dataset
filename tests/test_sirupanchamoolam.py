import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


DATA_PATH = (
    ROOT
    / "data"
    / "literature"
    / "sirupanchamoolam.json"
)


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def test_total_records(data):

    assert len(data) == 108, (
        f"Expected 108 records, found {len(data)}"
    )

    print("✓ Total Sirupanchamoolam records: 108")


def test_unique_ids(data):

    ids = [item["id"] for item in data]

    assert len(ids) == len(set(ids)), "Duplicate IDs found"

    print("✓ Unique IDs verified")


def test_schema(data):

    required_fields = [
        "id",
        "verseNumber",
        "tamilText",
        "simpleTamilMeaning",
        "moral",
        "englishMeaning",
        "transliteration",
        "keywords",
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

    missing_verses = 0
    missing_explanations = 0
    missing_morals = 0


    for item in data:

        if not item["tamilText"].strip():
            missing_verses += 1

        if not item["simpleTamilMeaning"].strip():
            missing_explanations += 1

        if not item["moral"].strip():
            missing_morals += 1


    print("\n===== Data Quality Report =====")

    print(f"Missing Verses          : {missing_verses}")
    print(f"Missing Explanations    : {missing_explanations}")
    print(f"Missing Morals          : {missing_morals}")


if __name__ == "__main__":

    print("\n===== TamilVerse Sirupanchamoolam Test =====\n")

    data = load_data()

    test_total_records(data)
    test_unique_ids(data)
    test_schema(data)
    quality_report(data)

    print("\n🎉 ALL SIRUPANCHAMOOLAM TESTS PASSED")