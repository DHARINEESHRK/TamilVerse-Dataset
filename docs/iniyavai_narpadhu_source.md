# Iniyavai Narpadhu Dataset Source

## Dataset Name

Pathinenkeezhkanakku - Iniyavai Narpadhu

---

## Literary Work

இனியவை நாற்பது (Iniyavai Narpadhu)

A classical Tamil ethical literature belonging to the Pathinen Keezhkanakku collection.

The work presents the virtues, good deeds, and desirable qualities that make human life meaningful.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/Pathinen_keezhkanakku-Iniyavainarpadhu

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

data/raw/iniyavai_narpadhu/iniyavai_narpadhu_raw.json

---

## Record Statistics

Expected Records:

41 poems

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

data/raw/iniyavai_narpadhu/iniyavai_narpadhu_raw.json

↓

Transformation Script:

scripts/transform_iniyavai_narpadhu.py

↓

Final Dataset:

data/literature/iniyavai_narpadhu.json

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

All transformations and future AI enrichment must happen through ETL scripts.

---

## TamilVerse Dataset Version

Version: v1.5

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending