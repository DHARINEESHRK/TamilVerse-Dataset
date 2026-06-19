import json
from pathlib import Path


# ==============================
# Paths
# ==============================

ROOT = Path(__file__).parent.parent

PAZHAMOZHI_PATH = (
    ROOT
    / "data"
    / "literature"
    / "pazhamozhi.json"
)


# ==============================
# Load Dataset
# ==============================

def load_data():
    with open(
        PAZHAMOZHI_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


# ==============================
# Test Total Records
# ==============================

def test_total_records(data):
    assert len(data) == 402, (
        f"Expected 402 records, found {len(data)}"
    )

    print("✓ Total Pazhamozhi records: 402")


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
# Test Schema Validation
# ==============================

def test_schema(data):

    required_fields = [
        "id",
        "title",
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
                f"Missing field {field} in ID {item.get('id')}"
            )

    print("✓ TamilVerse schema validation passed")


# ==============================
# Data Quality Report
# ==============================

def data_quality_report(data):

    missing_title = []
    missing_verse = []
    missing_explanation = []
    missing_moral = []


    for item in data:

        if not item["title"].strip():
            missing_title.append(item["id"])

        if not item["tamilText"].strip():
            missing_verse.append(item["id"])

        if not item["simpleTamilMeaning"].strip():
            missing_explanation.append(item["id"])

        if not item["moral"].strip():
            missing_moral.append(item["id"])


    print("\n===== Data Quality Report =====")

    print(
        f"Missing Topics          : {len(missing_title)}"
    )

    print(
        f"Missing Verses          : {len(missing_verse)}"
    )

    print(
        f"Missing Explanations    : {len(missing_explanation)}"
    )

    print(
        f"Missing Morals          : {len(missing_moral)}"
    )


# ==============================
# Run All Tests
# ==============================

if __name__ == "__main__":

    print(
        "\n===== TamilVerse Pazhamozhi Test =====\n"
    )

    data = load_data()

    test_total_records(data)

    test_unique_ids(data)

    test_schema(data)

    data_quality_report(data)

    print(
        "\n🎉 ALL PAZHAMOZHI TESTS PASSED"
    )