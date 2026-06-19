# Thirikadugam Dataset Source

## Dataset Name

Pathinenkeezhkanakku - Thirikadugam

---

## Literary Work

திரிகடுகம் (Thirikadugam)

A classical Tamil ethical literature belonging to the Pathinen Keezhkanakku collection.

The work contains moral teachings, wisdom, and life principles through concise poetic verses.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/Pathinen_keezhkanakku-Thirikadugam

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

data/raw/thirikadugam/thirikadugam_raw.json

---

## Record Statistics

Expected Records:

107 poems

---

## Original Dataset Schema

```json
{
    "poem": "",
    "explanation": ""
}
```

---

## Dataset Quality

Original Poem:
✓ Available

Tamil Explanation:
✓ Available

English Translation:
✗ Future AI Enrichment

Transliteration:
✗ Future AI Enrichment

Keywords:
✗ Future AI Enrichment

Moral:
✗ Future AI Enrichment

---

## TamilVerse Transformation Pipeline

Raw Dataset:

data/raw/thirikadugam/thirikadugam_raw.json

↓

Transformation Script:

scripts/transform_thirikadugam.py

↓

Final Dataset:

data/literature/thirikadugam.json

---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "tamilText": "",
    "simpleTamilMeaning": "",
    "englishMeaning": "",
    "transliteration": "",
    "keywords": [],
    "moral": "",
    "difficulty": "intermediate",
    "quiz": []
}
```

---

## Preservation Policy

Raw datasets must never be modified.

All transformations and future AI enrichment must be performed through ETL scripts.

---

## TamilVerse Dataset Version

Version: v1.1

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending