# Seevaga Chintamani Dataset Source

## Dataset Name

Aimperum Kaappiyangal - Seevaga Chintamani

---

## Literary Work

சீவக சிந்தாமணி (Seevaga Chintamani)

One of the five great Tamil epics (Aimperum Kaappiyangal).

It is a Jain Tamil epic known for its poetic richness, philosophical ideas, heroism, and spiritual teachings.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/aimperum_kaappiyangal-seevaga_chintamani

---

## Original Format

Nested JSON Dataset

Downloaded and preserved as:

data/raw/seevaga_chintamani/seevaga_chintamani_raw.json

---

## Original Dataset Schema

```json
{
    "title": "",
    "poems": [
        {
            "number": 1,
            "poem": ""
        }
    ]
}
```

---

## Dataset Quality

Section:
✓ Available

Verse Number:
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

data/raw/seevaga_chintamani/seevaga_chintamani_raw.json

↓

Transformation Script:

scripts/transform_seevaga_chintamani.py

↓

Final Dataset:

data/literature/seevaga_chintamani.json

---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "section": "",
    "verseNumber": 1,
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

All transformations and future AI enrichment must be performed through ETL scripts.

---

## TamilVerse Dataset Version

Version: v2.4

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending