import nltk
from nltk.corpus import wordnet as wn

# Download necessary resources if not already present
nltk.download('wordnet')
nltk.download('omw-1.4')

def find_related_words(word_root):
    # We'll collect all words related to the given root
    related_words = set()
    
    # Search all synsets in WordNet
    for synset in wn.all_synsets():
        # Check each lemma in the synset
        for lemma in synset.lemmas():
            word = lemma.name()
            # Check if the word contains the provided root
            if word_root.lower() in word.lower():
                related_words.add(word.lower())  # Add the word to the set (to avoid duplicates)
    
    return sorted(list(related_words))

def main():
    # Ask the user for a word root
    word_root = input("Enter a word root to search for related words: ").strip()
    
    # Check if the user entered something
    if word_root:
        related_words = find_related_words(word_root)
        
        if related_words:
            print(f"\nWords related to the root '{word_root}':")
            for word in related_words:
                print(word)
        else:
            print(f"\nNo words found related to the root '{word_root}'.")
    else:
        print("You must enter a word root.")

# Run the program
if __name__ == "__main__":
    main()

