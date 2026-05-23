# Roget's Adjective Extractor

A Python NLP experiment for extracting adjectives from a Roget's Thesaurus text file.

## Overview

This project uses NLTK part-of-speech tagging to identify adjectives in a text file. It was originally created as part of a larger adjective categorizer project using Roget's Thesaurus.

The project is exploratory: one important finding is that POS tagging words outside of sentence context can be unreliable. Many adjective-like entries in a thesaurus may be missed or misclassified because taggers perform best when they have surrounding sentence context.

## Features

- Reads a plain text file
- Tokenizes text with NLTK
- Tags each token with a part-of-speech label
- Extracts comparative, superlative, and standard adjectives
- Exports extracted adjectives to a text file

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```
Download required NLTK data:
```python
import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
```

## How to Run
```bash
python rogets_adjective_extractor.py
```
You will be prompted for:
1. The input `.txt` file path
2. The output `.txt` filename`
### Example
```txt
Enter input .txt file path: data/rogets_sample.txt
Enter output .txt filename: outputs/adjectives.txt
```
## Limitations
This script depends on NLTK's POS tagger, which works best with sentence context. Because Roget's Thesaurus entries are often lists, fragments, or isolated words, the output may miss valid adjectives or incorrectly tag some words.

## Skills Demonstrated
* Python scripting
* Natural language processing
* Part-of-speech tagging
* Text pre-processing
* Lexical analysis
* Experimental corpus work

## Future Improvements
* Compare NLTK output with a dictionary-based adjective list
* Add support for CSV output
* Remove duplicate adjectives
* Count adjective frequencies
* Preserve Roget category/head metadata
* Improve extraction using thesaurus structure instead of POS tagging alone
