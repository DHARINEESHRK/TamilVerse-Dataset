import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


DATA_PATH = (
    ROOT
    / "data"
    / "proverbs"
    / "tamil_proverbs.json"
)


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def test_total_records(data):

    assert len(data) == 1051, (
        f"Expected 1051 records, found {len(data)}"
    )

    print("✓ Total Tamil Proverbs records: 1051")


def test_unique_ids(data):

    ids = [item["id"] for item in data]

    assert len(ids) == len(set(ids)), (
        "Duplicate IDs found"
    )

    print("✓ Unique IDs verified")


def test_schema(data):

    required_fields = [
        "id",
        "proverb",
        "transliteration",
        "simpleTamilMeaning",
        "englishMeaning",
        "moral",
        "category",
        "difficulty"
    ]


    for item in data:

        for field in required_fields:

            assert field in item, (
                f"Missing {field} in ID {item['id']}"
            )

    print("✓ TamilVerse schema validation passed")


def quality_report(data):

    missing_proverbs = 0
    missing_transliteration = 0
    missing_english = 0


    for item in data:

        if not item["proverb"].strip():
            missing_proverbs += 1

        if not item["transliteration"].strip():
            missing_transliteration += 1

        if not item["englishMeaning"].strip():
            missing_english += 1


    print("\n===== Data Quality Report =====")

    print(
        f"Missing Proverbs          : {missing_proverbs}"
    )

    print(
        f"Missing Transliteration   : {missing_transliteration}"
    )

    print(
        f"Missing English Meaning   : {missing_english}"
    )


if __name__ == "__main__":

    print(
        "\n===== TamilVerse Proverbs Test =====\n"
    )

    data = load_data()

    test_total_records(data)
    test_unique_ids(data)
    test_schema(data)
    quality_report(data)

    print(
        "\n🎉 ALL PROVERBS TESTS PASSED"
    )
    