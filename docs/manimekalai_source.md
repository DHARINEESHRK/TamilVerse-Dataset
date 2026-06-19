# Manimekalai Dataset Source

## Dataset Name

Aimperum Kaappiyangal - Manimekalai

---

## Literary Work

மணிமேகலை (Manimekalai)

One of the five great Tamil epics (Aimperum Kaappiyangal).

It is a Buddhist Tamil epic that explores philosophy, morality, compassion, renunciation, and spiritual enlightenment.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/aimperum_kaappiyangal-manimekalai

---

## Original Format

Nested JSON Dataset

Downloaded and preserved as:

data/raw/manimekalai/manimekalai_raw.json

---

## Original Dataset Schema

```json
{
    "kaathai": "",
    "poems": [
        {
            "number": "",
            "poem": ""
        }
    ]
}
```

---

## Dataset Quality

Kaathai:
✓ Available

Poem Number:
✓ Available

Original Poem:
✓ Available

Tamil Explanation:
✗ Not Available in Source

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

data/raw/manimekalai/manimekalai_raw.json

↓

Transformation Script:

scripts/transform_manimekalai.py

↓

Final Dataset:

data/literature/manimekalai.json

---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "kaathai": "",
    "poemNumber": "",
    "tamilText": "",
    "simpleTamilMeaning": "",
    "englishMeaning": "",
    "transliteration": "",
    "keywords": [],
    "moral": "",
    "difficulty": "advanced",
    "quiz": []
}
```

---

## Preservation Policy

Raw datasets must never be modified.

All transformation and future AI enrichment must be performed through ETL scripts.

---

## TamilVerse Dataset Version

Version: v2.2

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending