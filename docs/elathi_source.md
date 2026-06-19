# Elathi Dataset Source

## Dataset Name

Pathinenkeezhkanakku - Elathi

---

## Literary Work

ஏலாதி (Elathi)

A classical Tamil ethical literature belonging to the Pathinen Keezhkanakku collection.

The work contains moral teachings, social values, and philosophical guidance through short poetic verses.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/pathinen_keezhkanakku-elathi

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

data/raw/elathi/elathi_raw.json

---

## Record Statistics

Expected Records:

82 verses

---

## Original Dataset Schema

```json
{
    "id": 1,
    "page": "",
    "blue_topic": "",
    "verse_number": 1,
    "verse": "",
    "explanation": "",
    "karuthurai": ""
}
```

---

## Dataset Quality

Topic:
✓ Available

Verse Number:
✓ Available

Original Verse:
✓ Available

Tamil Explanation:
✓ Available

Moral Explanation:
✓ Available

English Translation:
✗ Future AI Enrichment

Transliteration:
✗ Future AI Enrichment

---

## TamilVerse Transformation Pipeline

Raw Dataset:

data/raw/elathi/elathi_raw.json

↓

Transformation Script:

scripts/transform_elathi.py

↓

Final Dataset:

data/literature/elathi.json

---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "title": "",
    "verseNumber": 1,
    "tamilText": "",
    "simpleTamilMeaning": "",
    "moral": "",
    "englishMeaning": "",
    "transliteration": "",
    "keywords": [],
    "difficulty": "intermediate",
    "quiz": []
}
```

---

## Preservation Policy

Raw datasets must never be modified.

All transformation, cleaning, and future AI enrichment must happen through ETL scripts.

---

## TamilVerse Dataset Version

Version: v1.0

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending