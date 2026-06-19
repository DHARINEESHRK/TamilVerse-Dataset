# Acharakovai Dataset Source

## Dataset Name

Pathinenkeezhkanakku - Acharakovai

---

## Literary Work

ஆசாரக்கோவை (Acharakovai)

A classical Tamil ethical literature belonging to the Pathinen Keezhkanakku collection.

The work focuses on discipline, morality, good conduct, social responsibility, and the principles of righteous living.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/Pathinen_keezhkanakku-Acharakovai

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

data/raw/acharakovai/acharakovai_raw.json

---

## Record Statistics

Expected Records:

101 poems

---

## Original Dataset Schema

```json
{
    "number": "1",
    "topic": "",
    "venbha": "",
    "poem": "",
    "explanation": "",
    "karuthurai": ""
}
```

---

## Dataset Quality

Poem Number:
✓ Available

Topic:
✓ Available

Poem Type:
✓ Available

Original Poem:
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

data/raw/acharakovai/acharakovai_raw.json

↓

Transformation Script:

scripts/transform_acharakovai.py

↓

Final Dataset:

data/literature/acharakovai.json

---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "poemNumber": 1,
    "title": "",
    "poemType": "",
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

Version: v1.2

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending