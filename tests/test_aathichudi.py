import json
from pathlib import Path


# ==============================
# Paths
# ==============================

ROOT = Path(__file__).parent.parent

AATHICHUDI_PATH = (
    ROOT
    / "data"
    / "literature"
    / "aathichudi.json"
)


# ==============================
# Load Dataset
# ==============================

def load_data():
    with open(
        AATHICHUDI_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


# ==============================
# Test Total Records
# ==============================

def test_total_records(data):
    assert len(data) == 109, (
        f"Expected 109 records, found {len(data)}"
    )

    print("✓ Total Aathichudi records: 109")


# ==============================
# Test Unique IDs
# ==============================

def test_unique_ids(data):
    ids = [
        item["id"]
        for item in data
    ]

    assert len(ids) == len(set(ids)), (
        "Duplicate IDs found"
    )

    print("✓ Unique IDs verified")


# ==============================
# Test Required Fields
# ==============================

def test_schema(data):

    required_fields = [
        "id",
        "tamilText",
        "wordMeaning",
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
                f"Missing field {field} in ID {item.get('id')}"
            )

        assert item["tamilText"].strip(), (
            f"Empty Tamil text in ID {item['id']}"
        )

    print("✓ TamilVerse schema validation passed")


# ==============================
# Data Quality Report
# ==============================

def data_quality_report(data):

    missing_meaning = 0
    missing_paraphrase = 0
    missing_translation = 0

    for item in data:

        if not item["wordMeaning"].strip():
            missing_meaning += 1

        if not item["simpleTamilMeaning"].strip():
            missing_paraphrase += 1

        if not item["englishMeaning"].strip():
            missing_translation += 1


    print("\n===== Data Quality Report =====")

    print(
        f"Missing Word Meanings      : {missing_meaning}"
    )

    print(
        f"Missing Tamil Explanations : {missing_paraphrase}"
    )

    print(
        f"Missing English Meanings   : {missing_translation}"
    )


# ==============================
# Run All Tests
# ==============================

if __name__ == "__main__":

    print(
        "\n===== TamilVerse Aathichudi Test =====\n"
    )

    data = load_data()

    test_total_records(data)

    test_unique_ids(data)

    test_schema(data)

    data_quality_report(data)

    print(
        "\n🎉 ALL AATHICHUDI TESTS PASSED"
    )