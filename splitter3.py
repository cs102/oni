import nltk
from nltk.corpus import cmudict, wordnet
import spacy

# Download necessary data
nltk.download('cmudict')
nltk.download('wordnet')
nlp = spacy.load("en_core_web_sm")
d = cmudict.dict()

def get_syllables(word):
    """Splits word into syllables using the CMU Pronouncing Dictionary."""
    word = word.lower()
    if word in d:
        # The dictionary returns a list of phonetic sounds. 
        # Vowels end with a digit (0, 1, or 2).
        phonemes = d[word][0]
        return phonemes
    return ["Word not in dictionary"]

def decompose_morphemes(word):
    """Identifies root via SpaCy/WordNet and strips affixes."""
    doc = nlp(word.lower())
    lemma = doc[0].lemma_ # This is our 'Root'
    
    # Simple heuristic to find prefix and suffix
    prefix = ""
    suffix = ""
    
    if word.lower().startswith(lemma):
        suffix = word[len(lemma):]
    elif word.lower().endswith(lemma):
        prefix = word[:word.lower().find(lemma)]
    else:
        # If the root is buried (e.g., 'unbelievable')
        parts = word.lower().split(lemma)
        prefix = parts[0] if len(parts) > 0 else ""
        suffix = parts[1] if len(parts) > 1 else ""

    return {
        "prefix": prefix,
        "root": lemma,
        "suffix": suffix
    }

# Example Usage
test_word = "extraordinary" 
syllables = get_syllables(test_word)
morphology = decompose_morphemes(test_word)

print(f"Word: {test_word}")
print(f"Syllable Phonemes: {syllables}")
print(f"Morphemes: {morphology}")
