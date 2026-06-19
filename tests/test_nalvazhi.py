import json
from pathlib import Path


ROOT = Path(__file__).parent.parent

DATA_PATH = (
    ROOT
    / "data"
    / "literature"
    / "nalvazhi.json"
)


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def test_total_records(data):
    assert len(data) == 41, (
        f"Expected 41 records, found {len(data)}"
    )

    print("✓ Total Nalvazhi records: 41")


def test_unique_ids(data):
    ids = [item["id"] for item in data]

    assert len(ids) == len(set(ids)), (
        "Duplicate IDs found"
    )

    print("✓ Unique IDs verified")


def test_schema(data):

    required_fields = [
        "id",
        "poemNumber",
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

    missing_poem = []
    missing_meaning = []

    for item in data:

        if not item["tamilText"].strip():
            missing_poem.append(item["id"])

        if not item["simpleTamilMeaning"].strip():
            missing_meaning.append(item["id"])


    print("\n===== Data Quality Report =====")

    print(f"Missing Poems           : {len(missing_poem)}")
    print(f"Missing Explanations    : {len(missing_meaning)}")


if __name__ == "__main__":

    print("\n===== TamilVerse Nalvazhi Test =====\n")

    data = load_data()

    test_total_records(data)
    test_unique_ids(data)
    test_schema(data)
    quality_report(data)

    print("\n🎉 ALL NALVAZHI TESTS PASSED")