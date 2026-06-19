# Naaladiyar Dataset Source

## Dataset Name

Pathinenkeezhkanakku - Naaladiyar

---

## Literary Work

நாலடியார் (Naaladiyar)

A classical Tamil ethical literature work belonging to the Pathinen Keezhkanakku (Eighteen Lesser Texts) collection.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/Pathinenkeezhkanakku-Naaladiyar

---

## Author

Ancient Tamil Jain Scholars

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

```
data/raw/naaladiyar/naaladiyar_raw.json
```

---

## Record Statistics

Expected Records:

```
402 poems
```

---

## Original Dataset Fields

Each record contains:

```json
{
    "topic": "",
    "poem": "",
    "explanation": "",
    "paal": "",
    "iyal": ""
}
```

---

## Dataset Quality

Tamil Poem:
✓ Available

Detailed Explanation:
✓ Available

Paal Classification:
✓ Available

Iyal Classification:
✓ Available

English Translation:
✗ Not Available

Transliteration:
✗ Not Available

---

## TamilVerse Transformation Plan

Raw Dataset:

```
data/raw/naaladiyar/naaladiyar_raw.json
```

↓

Transformation Script:

```
scripts/transform_naaladiyar.py
```

↓

Final Dataset:

```
data/literature/naaladiyar.json
```

---

## TamilVerse Final Schema

```json
{
    "id": 1,

    "title": "",

    "tamilText": "",

    "simpleTamilMeaning": "",

    "paal": "",

    "iyal": "",

    "englishMeaning": "",

    "transliteration": "",

    "keywords": [],

    "moral": "",

    "difficulty": "intermediate",

    "quiz": []
}
```

---

## AI Enrichment (Future)

The following fields will be generated using AI:

- English translation
- Transliteration
- Keywords
- Moral extraction
- Difficulty adjustment
- Quiz generation
- Child-friendly explanation
- Adult scholarly explanation

---

## Preservation Policy

The raw dataset must never be modified.

All cleaning, schema conversion, enrichment, and validation must happen through transformation scripts.

---

## TamilVerse Dataset Version

Version: v0.5

Status:

✓ Raw dataset acquired  
✓ Dataset inspected  
✓ Documentation completed  
⬜ Transformation pending  
⬜ Validation pending  
⬜ Production integration pending