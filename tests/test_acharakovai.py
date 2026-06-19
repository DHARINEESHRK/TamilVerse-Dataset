import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


DATA_PATH = (
    ROOT
    / "data"
    / "literature"
    / "acharakovai.json"
)


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def test_total_records(data):

    assert len(data) == 101, (
        f"Expected 101 records, found {len(data)}"
    )

    print("✓ Total Acharakovai records: 101")


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
        "title",
        "poemType",
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

    missing_fields = {
        "Topics": 0,
        "Poem Types": 0,
        "Poems": 0,
        "Explanations": 0,
        "Morals": 0
    }

    for item in data:
        if not item["title"].strip():
            missing_fields["Topics"] += 1

        if not item["poemType"].strip():
            missing_fields["Poem Types"] += 1

        if not item["tamilText"].strip():
            missing_fields["Poems"] += 1

        if not item["simpleTamilMeaning"].strip():
            missing_fields["Explanations"] += 1

        if not item["moral"].strip():
            missing_fields["Morals"] += 1


    print("\n===== Data Quality Report =====")

    for key, value in missing_fields.items():
        print(f"Missing {key:<14}: {value}")


if __name__ == "__main__":

    print("\n===== TamilVerse Acharakovai Test =====\n")

    data = load_data()

    test_total_records(data)
    test_unique_ids(data)
    test_schema(data)
    quality_report(data)

    print("\n🎉 ALL ACHARAKOVAI TESTS PASSED")