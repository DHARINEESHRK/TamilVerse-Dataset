import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


DATA_PATH = (
    ROOT
    / "data"
    / "literature"
    / "elathi.json"
)


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def test_total_records(data):

    assert len(data) == 82, (
        f"Expected 82 records, found {len(data)}"
    )

    print("✓ Total Elathi records: 82")


def test_unique_ids(data):

    ids = [
        item["id"]
        for item in data
    ]

    assert len(ids) == len(set(ids)), (
        "Duplicate IDs found"
    )

    print("✓ Unique IDs verified")


def test_schema(data):

    required_fields = [
        "id",
        "title",
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

    missing_topics = []
    missing_verses = []
    missing_explanations = []
    missing_morals = []


    for item in data:

        if not item["title"].strip():
            missing_topics.append(item["id"])

        if not item["tamilText"].strip():
            missing_verses.append(item["id"])

        if not item["simpleTamilMeaning"].strip():
            missing_explanations.append(item["id"])

        if not item["moral"].strip():
            missing_morals.append(item["id"])


    print("\n===== Data Quality Report =====")

    print(f"Missing Topics          : {len(missing_topics)}")
    print(f"Missing Verses          : {len(missing_verses)}")
    print(f"Missing Explanations    : {len(missing_explanations)}")
    print(f"Missing Morals          : {len(missing_morals)}")


if __name__ == "__main__":

    print("\n===== TamilVerse Elathi Test =====\n")

    data = load_data()

    test_total_records(data)
    test_unique_ids(data)
    test_schema(data)
    quality_report(data)

    print("\n🎉 ALL ELATHI TESTS PASSED")