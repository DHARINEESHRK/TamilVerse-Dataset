# Konraiventhan Dataset Source

## Dataset Name

Avvaiyar - Konraiventhan

---

## Literary Work

கொன்றைவேந்தன் (Konraiventhan)

A classical Tamil moral literature work written by the great Tamil poet Avvaiyar.

It contains short ethical teachings, life lessons, and values suitable for young learners.

---

## Source Provider

TamilThagaval

---

## Source Platform

Hugging Face Dataset

---

## Source URL

https://huggingface.co/datasets/TamilThagaval/avvaiyar-konraiventan

---

## Original Format

Hugging Face Dataset

Downloaded and preserved as:

data/raw/konraiventhan/konraiventhan_raw.json

---

## Record Statistics

Expected Records:

92 poems

---

## Original Dataset Fields

Each record contains:

```json
{
    "Section": "",
    "Poem Line": "",
    "Explanation": ""
}
```

---

## Dataset Quality

Section:
✓ Available

Original Poem:
✓ Available

Tamil Explanation:
✓ Available

English Translation:
✗ Not Available

Transliteration:
✗ Not Available

---

## TamilVerse Transformation Plan


Raw Dataset:

data/raw/konraiventhan/konraiventhan_raw.json

↓
Transformation Script:

scripts/transform_konraiventhan.py

↓
Final Dataset:

data/literature/konraiventhan.json


---

## TamilVerse Final Schema

```json
{
    "id": 1,
    "title": "",
    "tamilText": "",
    "simpleTamilMeaning": "",
    "englishMeaning": "",
    "transliterati
```