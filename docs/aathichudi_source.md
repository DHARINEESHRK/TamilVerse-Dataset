# Aathichudi Dataset Source

## Dataset Name
Aathichudi

## Author
Avvaiyar

## Source Repository
tk120404/Aathichudi

## Source URL
https://github.com/tk120404/Aathichudi

## Dataset Type
Classical Tamil Moral Literature

## Original Format
JSON

## Raw Data Location

data/raw/aathichudi/aathichudi.json

## Record Statistics

Total Records: 109

Available Fields:
- number
- poem
- meaning
- paraphrase
- translation

## Data Quality Report

Tamil Poems:
109 / 109 available

Word Meanings:
108 / 109 available

Simple Tamil Explanations:
108 / 109 available

English Translations:
109 / 109 available

Missing Data:
- 1 record missing word meaning
- 1 record missing Tamil paraphrase

## Transformation Pipeline

Raw Dataset:
data/raw/aathichudi/aathichudi.json

        ↓

Transformation Script:
scripts/transform_aathichudi.py

        ↓

Final TamilVerse Dataset:
data/literature/aathichudi.json


## TamilVerse Final Schema

{
    "id": 1,
    "tamilText": "அறஞ்செய விரும்பு",
    "wordMeaning": "",
    "simpleTamilMeaning": "",
    "englishMeaning": "",
    "transliteration": "",
    "keywords": [],
    "moral": "",
    "difficulty": "beginner",
    "quiz": []
}

## AI Enrichment Status

Pending Future Enhancement:

- Transliteration generation
- Missing meaning completion
- Missing Tamil explanation completion
- Keyword extraction
- Moral category tagging
- Difficulty classification
- Quiz generation

## Preservation Policy

The original source dataset inside `data/raw/aathichudi/`
must never be modified.

All cleaning, restructuring, and enhancement operations must be performed through transformation scripts to maintain a reproducible data pipeline.

## TamilVerse Dataset Version

Version: v0.4

Status:
✓ Raw Dataset Acquired  
✓ Dataset Inspected  
✓ Transformation Completed  
✓ Schema Applied  
✓ Ready for Validation Testing