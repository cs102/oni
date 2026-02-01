import spacy

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

# Simple definitions
definitions = {
    "happy": "feeling or showing pleasure",
    "happiness": "the state of being happy",
    "unhappiness": "the state of not being happy",
    "careful": "done with attention",
    "care": "attention or concern",
}

def analyze_word(word):
    doc = nlp(word)
    token = doc[0]

    lemma = token.lemma_
    prefix = ""
    suffix = ""
    root = lemma

    # Find prefix
    for p in prefixes:
        if lemma.startswith(p) and len(lemma) > len(p):
            prefix = p
            root = lemma[len(p):]
            break

    # Find suffix
    for s in suffixes:
        if root.endswith(s) and len(root) > len(s):
            suffix = s
            root = root[:-len(s)]
            break

    print(f"\n🔍 Word: {word}")
    print(f"Lemma (spaCy): {lemma}")

    if prefix:
        print(f"Prefix: {prefix} — {prefixes[prefix]}")
    else:
        print("Prefix: None")

    print(f"Root: {root} — {definitions.get(root, 'Definition not found')}")

    if suffix:
        print(f"Suffix: {suffix} — {suffixes[suffix]}")
    else:
        print("Suffix: None")

    print(f"\n📘 Word Definition: {definitions.get(word, 'Definition not found')}")

# Run program
user_word = input("Enter a word: ").lower()
analyze_word(user_word)

