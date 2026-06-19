import json
from pathlib import Path


# ==========================
# Paths
# ==========================

ROOT = Path(__file__).parent.parent

THIRUKKURAL_PATH = (
    ROOT /
    "data" /
    "literature" /
    "thirukkural.json"
)


# ==========================
# Load Dataset
# ==========================

def load_data():
    with open(
        THIRUKKURAL_PATH,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


# ==========================
# Test Total Records
# ==========================

def test_total_kurals(data):
    assert len(data) == 1330, (
        f"Expected 1330 Kurals, found {len(data)}"
    )

    print("✓ Total Kurals: 1330")


# ==========================
# Test Unique IDs
# ==========================

def test_unique_ids(data):
    ids = [
        item["id"]
        for item in data
    ]

    assert len(ids) == len(set(ids)), (
        "Duplicate IDs found"
    )

    print("✓ Unique IDs")


# ==========================
# Test Kural Numbers
# ==========================

def test_kural_numbers(data):
    numbers = [
        item["kuralNumber"]
        for item in data
    ]

    assert len(numbers) == len(set(numbers)), (
        "Duplicate Kural Numbers found"
    )

    assert min(numbers) == 1
    assert max(numbers) == 1330

    print("✓ Kural numbers 1-1330")


# ==========================
# Test Chapters
# ==========================

def test_chapters(data):

    chapter_count = {}

    for item in data:
        chapter = item["chapterNumber"]

        chapter_count[chapter] = (
            chapter_count.get(chapter, 0) + 1
        )

    assert len(chapter_count) == 133, (
        f"Expected 133 chapters, found {len(chapter_count)}"
    )

    for chapter, count in chapter_count.items():
        assert count == 10, (
            f"Chapter {chapter} has {count} Kurals"
        )

    print("✓ 133 chapters with 10 Kurals each")


# ==========================
# Test Required Fields
# ==========================

def test_schema(data):

    required_fields = [
        "id",
        "kuralNumber",
        "chapterNumber",
        "chapter",
        "tamilText",
        "transliteration",
        "englishMeaning",
        "simpleTamilMeaning",
        "keywords",
        "moral",
        "difficulty",
        "quiz"
    ]

    for item in data:

        for field in required_fields:
            assert field in item, (
                f"Missing field {field}"
            )

        assert (
            item["tamilText"]["line1"].strip()
        ), "Missing line 1"

        assert (
            item["tamilText"]["line2"].strip()
        ), "Missing line 2"

    print("✓ Schema validation passed")


# ==========================
# Run All Tests
# ==========================

if __name__ == "__main__":

    print("\n===== TamilVerse Thirukkural Test =====\n")

    data = load_data()

    test_total_kurals(data)

    test_unique_ids(data)

    test_kural_numbers(data)

    test_chapters(data)

    test_schema(data)

    print("\n🎉 ALL THIRUKKURAL TESTS PASSED")