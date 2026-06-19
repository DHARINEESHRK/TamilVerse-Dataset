import json
from pathlib import Path


ROOT = Path(__file__).parent.parent


DATA_PATH = (
    ROOT
    / "data"
    / "literature"
    / "kundalakesi.json"
)


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def test_total_records(data):

    assert len(data) == 24, (
        f"Expected 24 records, found {len(data)}"
    )

    print("✓ Total Kundalakesi records: 24")


def test_unique_ids(data):

    ids = [item["id"] for item in data]

    assert len(ids) == len(set(ids))

    print("✓ Unique IDs verified")


def test_schema(data):

    required_fields = [
        "id",
        "section",
        "poemNumber",
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

            assert field in item


    print("✓ TamilVerse schema validation passed")


def quality_report(data):

    missing_titles = 0
    missing_poems = 0


    for item in data:

        if not item["title"].strip():
            missing_titles += 1

        if not item["tamilText"].strip():
            missing_poems += 1


    print("\n===== Data Quality Report =====")

    print(
        f"Missing Poem Titles     : {missing_titles}"
    )

    print(
        f"Missing Poems           : {missing_poems}"
    )


if __name__ == "__main__":

    print(
        "\n===== TamilVerse Kundalakesi Test =====\n"
    )


    data = load_data()


    test_total_records(data)
    test_unique_ids(data)
    test_schema(data)
    quality_report(data)


    print(
        "\n🎉 ALL KUNDALAKESI TESTS PASSED"
    )