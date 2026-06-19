# Naanmanikadigai Dataset Source

## Dataset Name

Pathinenkeezhkanakku - Naanmanikadigai

---

## Literary Work

நான்மணிக்கடிகை (Naanmanikadigai)

A classical Tamil ethical literature belonging to the Pathinen Keezhkanakku collection.

The work contains moral ideas, philosophical thoughts, and ethical teachings expressed through short poems.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/Pathinenkeezhkanakku-Naanmanikadikai

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

data/raw/naanmanikadigai/naanmanikadigai_raw.json

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

data/raw/naanmanikadigai/naanmanikadigai_raw.json

↓

Transformation Script:

scripts/transform_naanmanikadigai.py

↓

Final Dataset:

data/literature/naanmanikadigai.json
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

All transformations, cleaning, and future AI enrichment must be performed through ETL scripts.

---

## TamilVerse Dataset Version

Version: v1.3

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending