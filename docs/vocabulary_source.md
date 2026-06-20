# Tamil Vocabulary Dataset Source

## Dataset Name

Tamil Vocabulary - 1500 Important Words

---

## Dataset Description

A structured Tamil vocabulary collection containing 1,500 commonly used Tamil words organized into multiple categories such as body parts, animals, birds, food, nature, emotions, places, actions, and daily-life vocabulary.

Each vocabulary record contains:

- English word
- Tamil word
- Tamil transliteration
- Category classification
- Difficulty level

---

## Source Provider

iLearnTamil

---

## Source Platform

Website

---

## Source URL

https://ilearntamil.com/1500-important-words-list-in-tamil/

---

## Original Format

Microsoft Excel (.xlsx)

Original dataset preserved as:

```
data/raw/vocabulary/tamil_vocabulary_raw.xlsx
```

---

## Original Source Structure

The source Excel file does not follow a standard table format.

Structure:

- Category headers are stored as rows.
- Vocabulary entries are listed under each category.

Example:

```
BODY PARTS – உடல் உறுப்புகள் – UDAL URUPPUKAL

1 | Abdomen | அடி வயிறு | Adi vayiru
2 | Back    | முதுகு     | Mudhugu
3 | Brain   | மூளை      | Moolai
```

---

## Source Statistics

Original Excel Rows:

- 1,617 rows

Extracted Vocabulary Records:

- 1,500 words

Category Header Rows:

- 117 rows

---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "category": "Body Parts",
    "englishWord": "Abdomen",
    "tamilWord": "அடி வயிறு",
    "transliteration": "Adi vayiru",
    "difficulty": "basic"
}
```

---

## Transformation Pipeline

Raw Dataset:

data/raw/vocabulary/tamil_vocabulary_raw.xlsx

↓

Transformation Script:

scripts/transform_vocabulary.py

↓

Final Dataset:

data/vocabulary/tamil_vocabulary.json

---

## Data Quality Report

English Words:

✓ Available for all 1500 records

Tamil Words:

✓ Available for all 1500 records

Transliteration:

⚠ 1 record missing in original source

Category:

✓ Derived from source category headers

---

## Data Cleaning Process

During ETL:

- Converted non-standard Excel structure into structured JSON
- Extracted category names from header rows
- Removed category rows from vocabulary records
- Generated sequential TamilVerse IDs
- Added difficulty classification

---

## Preservation Policy

The original Excel file must never be modified.

All cleaning, transformations, and future enrichments must be handled through ETL scripts.

---

## TamilVerse Dataset Version

Version: v3.0

Status:

✓ Dataset Acquired  
✓ Dataset Inspected  
✓ Documentation Completed  
✓ Transformation Completed  
⬜ Validation Pending
