# TamilVerse Dataset

A comprehensive open-source Tamil language dataset designed for NLP, AI, educational applications, and Tamil language preservation.

## Project Vision

TamilVerse aims to create a structured, high-quality, machine-readable collection of Tamil literary and language resources with automated ETL pipelines, validation tests, and future AI enrichment.

---

# Current Dataset Statistics

## Total Verified Records

```
Tamil Alphabet        : 247
Classical Literature  : 5,122
-----------------------------
Total Records         : 5,369
```

## Automated Testing Status

```
Total Test Suites : 19
Passed            : 19
Failed            : 0
```

---

# Dataset Collections

## Tamil Alphabet (247)

- Uyir Ezhuthukkal (12)
- Mei Ezhuthukkal (18)
- Uyirmei Ezhuthukkal (216)
- Aytham (1)

---

# Classical Literature (5,122)

## Thirukkural

- 1,330 Kurals
- 133 Chapters

---

## Avvaiyar Literature

- Aathichudi (109)
- Konraiventhan (92)
- Nalvazhi (41)
- Moodurai (31)

---

## Pathinen Keezhkanakku

- Naaladiyar (402)
- Pazhamozhi Naanooru (402)
- Elathi (82)
- Thirikadugam (107)
- Acharakovai (101)
- Naanmanikadigai (107)
- Sirupanchamoolam (108)
- Iniyavai Narpadhu (41)
- Inna Narpadhu (41)

---

## Aimperum Kaappiyangal

- Kundalakesi (24)
- Silappadhikaram (1,047)
- Manimekalai (493)
- Valaiyapathi (72)
- Seevaga Chintamani (492)

---

# Project Structure

```
TamilVerse-Dataset/
│
├── data/
│   ├── raw/                  # Original source datasets
│   ├── literature/           # Transformed literature datasets
│   └── alphabet/             # Tamil alphabet datasets
│
├── scripts/
│   ├── download_*.py         # Dataset download scripts
│   └── transform_*.py        # ETL transformation scripts
│
├── tests/
│   └── test_*.py             # Automated validation tests
│
├── docs/
│   ├── *_source.md           # Dataset source documentation
│   └── data_issues.md        # Known source issues
│
├── requirements.txt
└── README.md
```

---

# ETL Workflow

Every dataset follows a consistent pipeline:

```
Download Source
        ↓
Inspect Raw Schema
        ↓
Transform Dataset
        ↓
Validate Data Quality
        ↓
Document Source Issues
        ↓
Version Control with Git
```

---

# Data Quality

## Validation Checks

Automated tests verify:

- Record counts
- Unique IDs
- Dataset schemas
- Missing fields
- Structural consistency

## Current Quality Status

- 5,369 records validated
- 19 automated test suites passed
- 0 transformation errors
- 100% documented source issues

---

# Known Source Issues

Some source datasets contain missing fields.

Examples:

- Missing original poems
- Missing explanations
- Missing moral explanations
- Missing poem titles
- Missing verse numbers

All known issues are documented in:

```
docs/data_issues.md
```

---

# Technology Stack

- Python
- JSON
- Hugging Face Datasets
- Automated ETL Pipelines
- Git & GitHub

---

# Future Roadmap

## TamilVerse v3.0

Planned datasets:

- Tamil vocabulary words
- Daily-use words
- Synonyms and antonyms
- Tamil paragraphs
- Reading comprehension passages
- Daily conversations
- Grammar resources

## AI Enrichment

Future enhancements:

- English translations
- Transliteration
- Keyword extraction
- Difficulty classification
- Quiz generation

---

# Contribution

Contributions are welcome.

You can contribute by:

- Fixing missing source data
- Adding new Tamil resources
- Improving ETL pipelines
- Improving validation tests
- Adding AI enrichment pipelines

---

# License

This project is open-source and intended for educational and research purposes.

---

# TamilVerse v2.4 Status

```
Dataset Completion        : Classical Foundation Completed
Total Records             : 5,369
Automated Tests           : 19/19 Passed
Transformation Errors     : 0
Source Issue Tracking     : Complete
Status                    : Production Ready
```

---

Preserving Tamil literature for the AI era.