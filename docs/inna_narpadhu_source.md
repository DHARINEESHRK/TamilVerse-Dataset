# Inna Narpadhu Dataset Source

## Dataset Name

Pathinenkeezhkanakku - Inna Narpadhu

---

## Literary Work

இன்னா நாற்பது (Inna Narpadhu)

A classical Tamil ethical literature belonging to the Pathinen Keezhkanakku collection.

The work describes actions, qualities, and situations that bring suffering and should be avoided in life.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/Pathinen_keezhkanakku-Innanarpadhu

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

data/raw/inna_narpadhu/inna_narpadhu_raw.json

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

data/raw/inna_narpadhu/inna_narpadhu_raw.json

↓

Transformation Script:

scripts/transform_inna_narpadhu.py

↓

Final Dataset:

data/literature/inna_narpadhu.json

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

Version: v1.6

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending