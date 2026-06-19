import json
import os


# Path to alphabet folder
BASE_PATH = os.path.join(
    "data",
    "alphabet"
)


# Expected counts
EXPECTED_COUNTS = {
    "uyir.json": 12,
    "mei.json": 18,
    "uyirmei.json": 216,
    "aytham.json": 1
}


# Required fields for every letter
REQUIRED_FIELDS = [
    "id",
    "letter",
    "category",
    "transliteration",
    "difficulty"
]


all_letters = []


def load_json(filename):
    path = os.path.join(BASE_PATH, filename)

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def test_counts():
    print("\nChecking letter counts...")

    total = 0

    for filename, expected in EXPECTED_COUNTS.items():
        data = load_json(filename)

        actual = len(data)

        assert actual == expected, (
            f"{filename}: Expected {expected}, found {actual}"
        )

        print(f"PASS {filename}: {actual} records")

        total += actual

    assert total == 247, (
        f"Total letters incorrect. Found {total}"
    )

    print("PASS Total Tamil characters: 247")


def test_required_fields():
    print("\nChecking required fields...")

    for filename in EXPECTED_COUNTS:
        data = load_json(filename)

        for item in data:
            for field in REQUIRED_FIELDS:
                assert field in item, (
                    f"{filename}: Missing '{field}' in {item}"
                )

    print("PASS All required fields exist")


def test_duplicates():
    print("\nChecking duplicates...")

    letters = []

    for filename in EXPECTED_COUNTS:
        data = load_json(filename)

        for item in data:
            letters.append(item["letter"])

    assert len(letters) == len(set(letters)), (
        "Duplicate Tamil letters found"
    )

    print("PASS No duplicate letters")


if __name__ == "__main__":

    print("========== TamilVerse Alphabet Test ==========")

    test_counts()

    test_required_fields()

    test_duplicates()

    print("\nALL TESTS PASSED")