import spacy
from nltk.corpus import wordnet as wn

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Prefixes and suffixes with meanings
prefixes = {
    "un": "not",
    "re": "again",
    "dis": "not or opposite of",
    "pre": "before",
    "mis": "wrongly"
}

suffixes = {
    "ness": "state or quality",
    "ful": "full of",
    "less": "without",
    "ly": "in a certain way",
    "ment": "action or process"
}

def get_definitions(word):
    """Return multiple WordNet definitions"""
    synsets = wn.synsets(word)
    if not synsets:
        return ["No definition found"]
    return [syn.definition() for syn in synsets]

def analyze_word(word):
    doc = nlp(word)
    token = doc[0]
    lemma = token.lemma_

    prefix = ""
    suffix = ""
    root = lemma

    # Detect prefix
    for p in prefixes:
        if lemma.startswith(p) and len(lemma) > len(p):
            prefix = p
            root = lemma[len(p):]
            break

    # Detect suffix
    for s in suffixes:
        if root.endswith(s) and len(root) > len(s):
            suffix = s
            root = root[:-len(s)]
            break

    print(f"\n🔍 Word: {word}")
    print(f"Lemma (spaCy): {lemma}")
    print(f"Part of Speech: {token.pos_}")

    # Prefix info
    if prefix:
        print(f"\nPrefix: {prefix}")
        print(f"Meaning: {prefixes[prefix]}")
    else:
        print("\nPrefix: None")

    # Root info
    print(f"\nRoot: {root}")
    print("Definitions:")
    for i, d in enumerate(get_definitions(root), 1):
        print(f"  {i}. {d}")

    # Suffix info
    if suffix:
        print(f"\nSuffix: {suffix}")
        print(f"Meaning: {suffixes[suffix]}")
    else:
        print("\nSuffix: None")

    # Full word definitions
    print(f"\n📘 Definitions of '{word}':")
    for i, d in enumerate(get_definitions(word), 1):
        print(f"  {i}. {d}")

# Run program
user_word = input("Enter a word: ").lower()
analyze_word(user_word)

