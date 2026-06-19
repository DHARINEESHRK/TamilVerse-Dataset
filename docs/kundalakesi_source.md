# Kundalakesi Dataset Source

## Dataset Name

Aimperum Kaappiyangal - Kundalakesi

---

## Literary Work

குண்டலகேசி (Kundalakesi)

One of the five great Tamil epics (Aimperum Kaappiyangal).

The surviving verses discuss philosophical thoughts, morality, impermanence of life, and spiritual understanding.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/aimperum_kaappiyangal-kundalakesi

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

data/raw/kundalakesi/kundalakesi_raw.json

---

## Record Statistics

Expected Records:

3 poems

---

## Original Dataset Schema

```json
{
    "title": "",
    "poems": [
        {
            "number": 1,
            "poem": "",
            "title": null
        }
    ]
}
```

---

## Dataset Quality

Section:
✓ Available

Poem Number:
✓ Available

Original Poem:
✓ Available

Poem Title:
✓ Partially Available

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

data/raw/kundalakesi/kundalakesi_raw.json

↓

Transformation Script:

scripts/transform_kundalakesi.py

↓

Final Dataset:

data/literature/kundalakesi.json

---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "section": "",
    "poemNumber": 1,
    "title": "",
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

All transformations and future AI enrichment must happen through ETL scripts.

---

## TamilVerse Dataset Version

Version: v2.0

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending