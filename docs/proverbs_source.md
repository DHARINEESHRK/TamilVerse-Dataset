# Tamil Proverbs Dataset Source

## Dataset Name

Tamil Proverbs - 1051 Proverbs

---

## Dataset Description

A structured collection of traditional Tamil proverbs containing Tamil sayings and their English translations.

Tamil proverbs represent centuries of wisdom, cultural knowledge, ethics, life lessons, and practical experiences passed down through generations.

---

## Source Provider

Selvakumarduraipandian

---

## Source Platform

Hugging Face Datasets

---

## Source Dataset

Selvakumarduraipandian/Tamil-Proverbs

---

## Original Format

JSON Dataset

Original dataset preserved as:

data/raw/proverbs/proverbs_raw.json

---

## Original Source Schema

```json
{
    "S.No": 1,
    "Tamil": "அகங்கையிற் போட்டுப் புறங்கையை நக்கலாமா?",
    "English": "Having placed the thing on the palm, why lick the back of the hand"
}
```

---

## Source Statistics

Total Records:

- 1051 Tamil Proverbs

---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "proverb": "அகங்கையிற் போட்டுப் புறங்கையை நக்கலாமா?",
    "simpleTamilMeaning": "",
    "englishMeaning": "Having placed the thing on the palm, why lick the back of the hand",
    "moral": "",
    "category": "",
    "difficulty": "basic"
}
```

---

## Field Mapping

| Original Field | TamilVerse Field |
|----------------|------------------|
| S.No | id |
| Tamil | proverb |
| English | englishMeaning |

---

## Dataset Quality

Tamil Proverb:

✓ Available for all records

English Meaning:

✓ Available for all records

Simple Tamil Meaning:

✗ Not available in source

Moral:

✗ Not available in source

Category:

✗ Not available in source

Difficulty:

✓ Added during transformation

---

## Transformation Pipeline

Raw Dataset:

data/raw/proverbs/proverbs_raw.json

↓

Transformation Script:

scripts/transform_proverbs.py

↓

Final Dataset:

data/proverbs/tamil_proverbs.json

---

## Preservation Policy

The original source dataset must never be modified.

All cleaning, transformations, and AI enrichments must be handled through ETL scripts.

---

## TamilVerse Dataset Version

Version: v3.1

Status:

✓ Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending