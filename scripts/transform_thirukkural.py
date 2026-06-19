import json
from pathlib import Path


# ==============================
# Paths
# ==============================

ROOT = Path(__file__).parent.parent

CHAPTERS_PATH = ROOT / "data" / "raw" / "thirukkural-dataset" / "chapters.txt"

KURAL_PATH = ROOT / "data" / "raw" / "thirukkural-dataset" / "thirukkural.txt"

OUTPUT_PATH = ROOT / "data" / "literature" / "thirukkural.json"


# ==============================
# Load Chapter Names
# ==============================

def load_chapters():
    with open(CHAPTERS_PATH, "r", encoding="utf-8") as file:
        chapters = [
            line.strip()
            for line in file
            if line.strip()
        ]

    return chapters


# ==============================
# Load Kurals
# ==============================

def load_kurals():
    with open(KURAL_PATH, "r", encoding="utf-8") as file:
        kurals = [
            line.strip()
            for line in file
            if line.strip()
        ]

    return kurals


# ==============================
# Transform Dataset
# ==============================

def transform():

    chapters = load_chapters()
    kurals = load_kurals()

    print(f"Chapters found: {len(chapters)}")
    print(f"Kurals found: {len(kurals)}")


    if len(chapters) != 133:
        raise Exception(
            "Invalid chapter count. Expected 133."
        )

    if len(kurals) != 1330:
        raise Exception(
            "Invalid kural count. Expected 1330."
        )


    dataset = []


    for index, kural in enumerate(kurals, start=1):

        # Every 10 kurals belong to one chapter
        chapter_index = (index - 1) // 10


        # Split two-line kural
        lines = kural.split("$")


        if len(lines) != 2:
            raise Exception(
                f"Kural {index} does not have exactly 2 lines."
            )


        record = {

            "id": index,

            "kuralNumber": index,


            "chapterNumber": chapter_index + 1,


            "chapter": chapters[chapter_index],


            "tamilText": {
                "line1": lines[0].strip(),
                "line2": lines[1].strip()
            },


            # Future AI enrichment fields
            "transliteration": "",

            "englishMeaning": "",

            "simpleTamilMeaning": "",


            "keywords": [],


            "moral": "",


            "difficulty": "beginner",


            "quiz": []

        }


        dataset.append(record)


    # Save final JSON
    with open(
        OUTPUT_PATH,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            dataset,
            file,
            ensure_ascii=False,
            indent=4
        )


    print("\nTransformation Complete")
    print(f"Generated records: {len(dataset)}")
    print(f"Saved to: {OUTPUT_PATH}")


# ==============================
# Main
# ==============================

if __name__ == "__main__":

    transform()