import json
from pathlib import Path


# ==============================
# Paths
# ==============================

ROOT = Path(__file__).parent.parent

DATA_PATH = (
    ROOT
    / "data"
    / "literature"
    / "konraiventhan.json"
)


# ==============================
# Load Dataset
# ==============================

def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


# ==============================
# Record Count Test
# ==============================

def test_total_records(data):
    assert len(data) == 92, (
        f"Expected 92 records, found {len(data)}"
    )

    print("✓ Total Konraiventhan records: 92")


# ==============================
# Unique ID Test
# ==============================

def test_unique_ids(data):
    ids = [item["id"] for item in data]

    assert len(ids) == len(set(ids)), (
        "Duplicate IDs found"
    )

    print("✓ Unique IDs verified")


# ==============================
# Schema Validation
# ==============================

def test_schema(data):

    required_fields = [
        "id",
        "title",
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


# ==============================
# Data Quality Report
# ==============================

def quality_report(data):

    missing_title = []
    missing_text = []
    missing_meaning = []

    for item in data:

        if not item["title"].strip():
            missing_title.append(item["id"])

        if not item["tamilText"].strip():
            missing_text.append(item["id"])

        if not item["simpleTamilMeaning"].strip():
            missing_meaning.append(item["id"])


    print("\n===== Data Quality Report =====")

    print(f"Missing Sections        : {len(missing_title)}")
    print(f"Missing Poems           : {len(missing_text)}")
    print(f"Missing Explanations    : {len(missing_meaning)}")


# ==============================
# Run Tests
# ==============================

if __name__ == "__main__":

    print("\n===== TamilVerse Konraiventhan Test =====\n")

    data = load_data()

    test_total_records(data)

    test_unique_ids(data)

    test_schema(data)

    quality_report(data)

    print("\n🎉 ALL KONRAIVENTHAN TESTS PASSED")