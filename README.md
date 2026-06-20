# TamilVerse v3.0

A comprehensive open-source Tamil language dataset designed for NLP, AI, educational applications, and Tamil language preservation.

---

## Current Dataset Statistics

```
Tamil Alphabet          : 247
Classical Literature    : 5,122
Tamil Vocabulary        : 1,500
--------------------------------
Total TamilVerse        : 6,869 Records
```

---

## Automated Testing Status

```
Total Test Suites       : 20
Passed                  : 20
Failed                  : 0
```

---

## Dataset Collections

### Tamil Alphabet (247)

- Uyir Ezhuthukkal (12)
- Mei Ezhuthukkal (18)
- Uyirmei Ezhuthukkal (216)
- Aytham (1)

---

### Classical Literature (5,122)

#### Thirukkural
- 1,330 Kurals
- 133 Chapters

#### Avvaiyar Literature
- Aathichudi (109)
- Konraiventhan (92)
- Nalvazhi (41)
- Moodurai (31)

#### Pathinen Keezhkanakku
- Naaladiyar (402)
- Pazhamozhi Naanooru (402)
- Elathi (82)
- Thirikadugam (107)
- Acharakovai (101)
- Naanmanikadigai (107)
- Sirupanchamoolam (108)
- Iniyavai Narpadhu (41)
- Inna Narpadhu (41)

#### Aimperum Kaappiyangal
- Kundalakesi (24)
- Silappadhikaram (1,047)
- Manimekalai (493)
- Valaiyapathi (72)
- Seevaga Chintamani (492)

---

### Tamil Vocabulary (1,500)

The Tamil Vocabulary dataset contains commonly used words collected from various real-life categories.

Included fields:

- English words
- Tamil words
- Transliteration
- Category classification
- Difficulty levels

---

## Data Quality & Validation

The TamilVerse project maintains a complete ETL and validation workflow.

Validation includes:

- Record count verification
- Unique ID checking
- Schema validation
- Missing data detection
- Dataset consistency checks

Current Quality Status:

- 6,869 verified records
- 20/20 automated tests passed
- 0 transformation errors
- 100% known source issues documented

---

## Known Dataset Issues

All missing or incomplete source data is documented in:

```
docs/data_issues.md
```

Current known issues include:

- Missing original poems from source datasets
- Missing explanations
- Missing moral explanations
- Missing poem titles
- Missing verse numbers
- Missing vocabulary transliteration

All missing fields originate from the original sources and are preserved for future manual verification or AI-assisted enrichment.

---

## TamilVerse v3.0 Status

```
✓ Tamil Alphabet Completed

✓ Classical Literature Completed

✓ Tamil Vocabulary Completed

✓ Automated ETL Pipeline Completed

✓ Automated Validation Suite Completed

✓ Data Issue Tracking Completed

Total Records:
6,869 Verified Tamil Records
```

---

## Technology Stack

- Python
- JSON
- Pandas
- OpenPyXL
- Hugging Face Datasets
- Automated ETL Pipelines
- Git & GitHub

---

## Future Roadmap

### TamilVerse v3.1

Upcoming datasets:

- Tamil Reading Paragraphs
- Reading Comprehension Questions
- Daily Conversations
- Tamil Grammar Resources
- Stories and Essays

---

### AI Enrichment Pipeline

Future enhancements:

- English translations for literature
- Tamil explanations
- Transliteration generation
- Keyword extraction
- Difficulty analysis
- Quiz generation

---

## Contribution

Contributions are welcome.

You can contribute by:

- Adding new Tamil datasets
- Improving ETL pipelines
- Creating validation tests
- Fixing source data issues
- Building AI enrichment tools

---

## License

Open-source project for educational, linguistic, and AI research purposes.

---

**Preserving Tamil knowledge for the AI era.**