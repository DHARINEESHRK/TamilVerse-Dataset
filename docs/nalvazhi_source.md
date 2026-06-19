# Nalvazhi Dataset Source

## Dataset Name

Avvaiyar - Nalvazhi

---

## Literary Work

நல்வழி (Nalvazhi)

A classical Tamil ethical literature written by Avvaiyar.

The work contains moral teachings, guidance for good character, discipline, wisdom, and proper ways of living.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/avvaiyar-nalvazhi

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

data/raw/nalvazhi/nalvazhi_raw.json

---

## Record Statistics

Expected Records:

41 poems

---

## Original Dataset Schema

```json
{
    "Poem No": "",
    "Poem Text": "",
    "Explanation": ""
}
```

---

## Dataset Quality

Poem Number:
✓ Available

Original Poem:
✓ Available

Tamil Explanation:
✓ Available

English Translation:
✗ Future AI enrichment

Transliteration:
✗ Future AI enrichment

---

## TamilVerse Transformation Pipeline

Raw Dataset:

data/raw/nalvazhi/nalvazhi_raw.json

↓

Transformation Script:

scripts/transform_nalvazhi.py

↓

Final Dataset:

data/literature/nalvazhi.json

---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "poemNumber": 0,
    "tamilText": "",
    "simpleTamilMeaning": "",
    "englishMeaning": "",
    "transliteration": "",
    "keywords": [],
    "moral": "",
    "difficulty": "beginner",
    "quiz": []
}
```

---

## Preservation Policy

The raw dataset must never be modified.

All cleaning, transformation, and enrichment must happen through ETL scripts.

---

## TamilVerse Dataset Version

Version: v0.8

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending