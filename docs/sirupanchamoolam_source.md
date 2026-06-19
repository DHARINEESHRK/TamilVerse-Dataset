# Sirupanchamoolam Dataset Source

## Dataset Name

Pathinenkeezhkanakku - Sirupanchamoolam

---

## Literary Work

சிறுபஞ்சமூலம் (Sirupanchamoolam)

A classical Tamil ethical literature belonging to the Pathinen Keezhkanakku collection.

The work contains moral teachings, virtues, and principles for a righteous life.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/pathinen_keezhkanakku-sirupanchamoolam

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

data/raw/sirupanchamoolam/sirupanchamoolam_raw.json

---

## Record Statistics

Expected Records:

108 verses

---

## Original Dataset Schema

```json
{
    "id": 0,
    "verse": "",
    "explanation": "",
    "karuthurai": ""
}
```

---

## Dataset Quality

Verse Number:
✓ Available

Original Verse:
✓ Available

Tamil Explanation:
✓ Available

Moral:
✓ Available

English Translation:
✗ Future AI Enrichment

Transliteration:
✗ Future AI Enrichment

---

## TamilVerse Transformation Pipeline

Raw Dataset:

data/raw/sirupanchamoolam/sirupanchamoolam_raw.json

↓

Transformation Script:

scripts/transform_sirupanchamoolam.py

↓

Final Dataset:

data/literature/sirupanchamoolam.json

---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "verseNumber": 0,
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

All cleaning, transformation, and future AI enrichment must happen through ETL scripts.

---

## TamilVerse Dataset Version

Version: v1.4

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending