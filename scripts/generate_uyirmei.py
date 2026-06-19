import json
import os


# Tamil vowel symbols (matras)
vowel_signs = [
    ("அ", ""),     
    ("ஆ", "ா"),
    ("இ", "ி"),
    ("ஈ", "ீ"),
    ("உ", "ு"),
    ("ஊ", "ூ"),
    ("எ", "ெ"),
    ("ஏ", "ே"),
    ("ஐ", "ை"),
    ("ஒ", "ொ"),
    ("ஓ", "ோ"),
    ("ஔ", "ௌ")
]


# Base consonants without pulli
mei_bases = [
    ("க", "k"),
    ("ங", "ng"),
    ("ச", "ch"),
    ("ஞ", "nj"),
    ("ட", "t"),
    ("ண", "n"),
    ("த", "th"),
    ("ந", "n"),
    ("ப", "p"),
    ("ம", "m"),
    ("ய", "y"),
    ("ர", "r"),
    ("ல", "l"),
    ("வ", "v"),
    ("ழ", "zh"),
    ("ள", "L"),
    ("ற", "R"),
    ("ன", "N")
]


# Transliteration for vowels
vowel_sounds = {
    "அ": "a",
    "ஆ": "aa",
    "இ": "i",
    "ஈ": "ii",
    "உ": "u",
    "ஊ": "uu",
    "எ": "e",
    "ஏ": "ee",
    "ஐ": "ai",
    "ஒ": "o",
    "ஓ": "oo",
    "ஔ": "au"
}


uyirmei_data = []

id_counter = 1


for consonant, sound in mei_bases:
    for vowel, symbol in vowel_signs:

        letter = consonant + symbol

        record = {
            "id": id_counter,
            "letter": letter,
            "category": "uyirmei",
            "baseConsonant": consonant + "்",
            "vowel": vowel,
            "transliteration": sound + vowel_sounds[vowel],
            "difficulty": "beginner",
            "examples": [],
            "description": f"Combination of {consonant} and {vowel}"
        }

        uyirmei_data.append(record)

        id_counter += 1


# Output path
output_path = os.path.join(
    "data",
    "alphabet",
    "uyirmei.json"
)


# Ensure folder exists
os.makedirs(
    os.path.dirname(output_path),
    exist_ok=True
)


# Save JSON
with open(
    output_path,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        uyirmei_data,
        file,
        ensure_ascii=False,
        indent=4
    )


print("✅ Uyirmei dataset generated successfully!")
print(f"Total letters created: {len(uyirmei_data)}")