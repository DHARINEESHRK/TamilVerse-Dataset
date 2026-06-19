# Moodurai Dataset Source

## Dataset Name

Avvaiyar - Moodurai

---

## Literary Work

மூதுரை (Moodurai)

A classical Tamil ethical literature written by Avvaiyar.

The work contains wisdom, moral values, social guidance, and principles for a good life.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/avvaiyar-moodurai

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

data/raw/moodurai/moodurai_raw.json

---

## Record Statistics

Expected Records:

31 poems

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
✗ Future AI Enrichment

Transliteration:
✗ Future AI Enrichment

---

## TamilVerse Transformation Pipeline

Raw Dataset:

data/raw/moodurai/moodurai_raw.json

↓

Transformation Script:

scripts/transform_moodurai.py

↓

Final Dataset:

data/literature/moodurai.json

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

Raw datasets must never be modified.

All cleaning, transformation, and enrichment should happen through ETL scripts.

---

## TamilVerse Dataset Version

Version: v0.9

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending