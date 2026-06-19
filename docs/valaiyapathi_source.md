# Valaiyapathi Dataset Source

## Dataset Name

Aimperum Kaappiyangal - Valaiyapathi

---

## Literary Work

வளையாபதி (Valaiyapathi)

One of the five great Tamil epics (Aimperum Kaappiyangal).

Valaiyapathi is a partially preserved Tamil epic containing philosophical ideas, ethical values, and reflections on human life.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/aimperum_kaappiyangal-valaiyapathi

---

## Original Format

Flat JSON Dataset

Downloaded and preserved as:

data/raw/valaiyapathi/valaiyapathi_raw.json

---

## Record Statistics

Expected Records:

72 poems

---

## Original Dataset Schema

```json
{
    "number": 1,
    "poem": ""
}
```

---

## Dataset Quality

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

data/raw/valaiyapathi/valaiyapathi_raw.json

↓

Transformation Script:

scripts/transform_valaiyapathi.py

↓

Final Dataset:

data/literature/valaiyapathi.json

---

## TamilVerse Final Schema

```json
{
    "id": 1,
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

Version: v2.3

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending