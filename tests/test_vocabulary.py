import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


DATA_PATH = (
    ROOT
    / "data"
    / "vocabulary"
    / "tamil_vocabulary.json"
)
def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def test_total_records(data):

    assert len(data) == 1500, (
        f"Expected 1500 records, found {len(data)}"
    )

    print("✓ Total Vocabulary records: 1500")


def test_unique_ids(data):

    ids = [item["id"] for item in data]

    assert len(ids) == len(set(ids)), (
        "Duplicate IDs found"
    )

    print("✓ Unique IDs verified")


def test_schema(data):

    required_fields = [
        "id",
        "category",
        "englishWord",
        "tamilWord",
        "transliteration",
        "difficulty"
    ]


    for item in data:

        for field in required_fields:

            assert field in item, (
                f"Missing {field} in ID {item['id']}"
            )


    print("✓ TamilVerse schema validation passed")


def quality_report(data):

    missing_categories = 0
    missing_english = 0
    missing_tamil = 0
    missing_transliteration = 0


    for item in data:

        if not item["category"].strip():
            missing_categories += 1

        if not item["englishWord"].strip():
            missing_english += 1

        if not item["tamilWord"].strip():
            missing_tamil += 1

        if not item["transliteration"].strip():
            missing_transliteration += 1


    print("\n===== Data Quality Report =====")

    print(
        f"Missing Categories        : {missing_categories}"
    )

    print(
        f"Missing English Words     : {missing_english}"
    )

    print(
        f"Missing Tamil Words       : {missing_tamil}"
    )

    print(
        f"Missing Transliteration   : {missing_transliteration}"
    )


if __name__ == "__main__":

    print(
        "\n===== TamilVerse Vocabulary Test =====\n"
    )


    data = load_data()


    test_total_records(data)
    test_unique_ids(data)
    test_schema(data)
    quality_report(data)


    print(
        "\n🎉 ALL VOCABULARY TESTS PASSED"
    )