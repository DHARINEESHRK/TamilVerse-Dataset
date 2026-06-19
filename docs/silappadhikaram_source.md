# Silappadhikaram Dataset Source

## Dataset Name

Aimperum Kaappiyangal - Silappadhikaram

---

## Literary Work

சிலப்பதிகாரம் (Silappadhikaram)

One of the five great Tamil epics (Aimperum Kaappiyangal).

The epic narrates the story of Kannagi and Kovalan and explores themes of justice, virtue, love, fate, and social values.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/aimperum_kaappiyangal-silappadhikaram

---

## Original Format

Nested JSON Dataset

Downloaded and preserved as:

data/raw/silappadhikaram/silappadhikaram_raw.json

---

## Original Dataset Schema

```json
{
    "kaandam": "",
    "kaathaigal": [
        {
            "kaathai": "",
            "poems": [
                {
                    "number": null,
                    "poem": ""
                }
            ]
        }
    ]
}
```

---

## Dataset Quality

Kaandam:
✓ Available

Kaathai:
✓ Available

Original Poem:
✓ Available

Poem Number:
⚠ Partially Available

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

data/raw/silappadhikaram/silappadhikaram_raw.json

↓

Transformation Script:

scripts/transform_silappadhikaram.py

↓

Final Dataset:

data/literature/silappadhikaram.json

---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "kaandam": "",
    "kaathai": "",
    "poemNumber": null,
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

Version: v2.1

Status:

✓ Raw Dataset Acquired
✓ Dataset Inspected
✓ Documentation Completed
⬜ Transformation Pending
⬜ Validation Pending
