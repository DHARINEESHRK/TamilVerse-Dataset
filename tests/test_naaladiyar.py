import json
from pathlib import Path


# ==============================
# Paths
# ==============================

ROOT = Path(__file__).parent.parent

NAALADIYAR_PATH = (
    ROOT
    / "data"
    / "literature"
    / "naaladiyar.json"
)


# ==============================
# Load Dataset
# ==============================

def load_data():
    with open(
        NAALADIYAR_PATH,
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

    print("✓ Total Naaladiyar records: 402")


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
        "paal",
        "iyal",
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

    print("✓ TamilVerse schema validation passed")


# ==============================
# Data Quality Report
# ==============================

def data_quality_report(data):

    missing_poems = []
    missing_explanations = []
    missing_paal = []
    missing_iyal = []


    for item in data:

        if not item["tamilText"].strip():
            missing_poems.append(item["id"])

        if not item["simpleTamilMeaning"].strip():
            missing_explanations.append(item["id"])

        if not item["paal"].strip():
            missing_paal.append(item["id"])

        if not item["iyal"].strip():
            missing_iyal.append(item["id"])


    print("\n===== Data Quality Report =====")

    print(
        f"Missing Poems            : {len(missing_poems)}"
    )

    if missing_poems:
        print(
            f"IDs: {missing_poems}"
        )


    print(
        f"Missing Explanations     : {len(missing_explanations)}"
    )

    print(
        f"Missing Paal             : {len(missing_paal)}"
    )

    print(
        f"Missing Iyal             : {len(missing_iyal)}"
    )


# ==============================
# Run All Tests
# ==============================

if __name__ == "__main__":

    print(
        "\n===== TamilVerse Naaladiyar Test =====\n"
    )

    data = load_data()

    test_total_records(data)

    test_unique_ids(data)

    test_schema(data)

    data_quality_report(data)


    print(
        "\n🎉 ALL NAALADIYAR TESTS PASSED"
    )