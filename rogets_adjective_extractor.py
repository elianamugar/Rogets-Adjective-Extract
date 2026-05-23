"""
Extract adjectives from a Roget's Thesaurus text file.

This script uses NLTK to tokenize and part-of-speech tag a text file,
then extracts words tagged as adjectives.
"""

from pathlib import Path

import nltk


ADJECTIVE_TAGS = {"JJ", "JJR", "JJS"}
EXCLUDED_WORDS = {"such"}


def extract_adjectives(text):
    """Return adjectives from input text using NLTK POS tags."""
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)

    adjectives = []

    for word, tag in tagged_tokens:
        if tag in ADJECTIVE_TAGS and word.lower() not in EXCLUDED_WORDS:
            adjectives.append(word)

    return adjectives


def main():
    """Run the Roget's adjective extraction workflow."""
    input_path = Path(input("Enter input .txt file path: ").strip())
    output_path = Path(input("Enter output .txt filename: ").strip())

    if not input_path.exists():
        print("Error: input file does not exist.")
        return

    text = input_path.read_text(encoding="utf-8")
    adjectives = extract_adjectives(text)

    output_path.write_text("\n".join(adjectives), encoding="utf-8")

    print(f"Extracted {len(adjectives)} adjectives.")
    print(f"Saved results to {output_path}")


if __name__ == "__main__":
    main()
