# Pazhamozhi Naanooru Dataset Source

## Dataset Name

Pathinenkeezhkanakku - Pazhamozhi Naanooru

---

## Literary Work

பழமொழி நானூறு (Pazhamozhi Naanooru)

A classical Tamil literary work belonging to the Pathinen Keezhkanakku (Eighteen Lesser Texts) collection.

The work contains traditional Tamil proverbs, ethical teachings, social wisdom, and practical life lessons.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/pathinen_keezhkanakku-pazhamozhinaanooru

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

```
data/raw/pazhamozhi/pazhamozhi_raw.json
```

---

## Record Statistics

Expected Records:

```
402 verses
```

---

## Original Dataset Fields

Each record contains:

```json
{
    "id": 1,
    "blue_topic": "",
    "verse": "",
    "explanation": "",
    "karuthurai": ""
}
```

---

## Dataset Quality

Topic:
✓ Available

Original Verse:
✓ Available

Detailed Tamil Explanation:
✓ Available

Moral Summary:
✓ Available

English Translation:
✗ Not Available

Transliteration:
✗ Not Available

---

## TamilVerse Transformation Plan

Raw Dataset:

```
data/raw/pazhamozhi/pazhamozhi_raw.json
```

↓

Transformation Script:

```
scripts/transform_pazhamozhi.py
```

↓

Final Dataset:

```
data/literature/pazhamozhi.json
```

---

## TamilVerse Final Schema

```json
{
    "id": 1,

    "title": "",

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

## AI Enrichment (Future)

The following fields will be generated using AI:

- English Translation
- Transliteration
- Keyword Extraction
- Vocabulary Generation
- Age-based Explanation
- Quiz Generation

---

## Preservation Policy

The raw dataset must never be modified.

All cleaning, transformation, enrichment, and validation must be performed through scripts to maintain a reproducible ETL pipeline.

---

## TamilVerse Dataset Version

Version: v0.6

Status:

✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
⬜ Transformation Pending  
⬜ Validation Pending  
⬜ Production Integration Pending