import nltk
from nltk.corpus import wordnet as wn
from collections import Counter
import os

# Download necessary resources if not already present
nltk.download('wordnet')
nltk.download('omw-1.4')

# file output with words
file_path = "output.txt"


def find_related_words(word_root):
    # We'll collect all words related to the given root in a list
    word_list = []
    
    # Search all synsets in WordNet
    for synset in wn.all_synsets():
        # Check each lemma in the synset
        for lemma in synset.lemmas():
            word = lemma.name()
            # Check if the word contains the provided root
            if word_root.lower() in word.lower():
                word_list.append(word.lower())  # Add the word to the list
    
    return word_list
    
def save_word_list(word_list):
    try:
        with open(file_path, "x", encoding="utf-8") as file:
            # str convers word_list to strings
            file.write("\n" + str(word_list))
            print(f"txt file '{file_path}' was created ^ ^ ")
    except FileExistsError:
        print("File already exist ⊙﹏⊙ ")

def main():
    # Ask the user for a word root
    word_root = input("Enter a word root to search for related words: ").strip()
    
    # Check if the user entered something
    if word_root:
        word_list = find_related_words(word_root)
        
        if word_list:
            # Count word frequencies using Counter from the collections module
            word_frequencies = Counter(word_list)
            
            # save word list
            save_word_list(word_list)

            # Sort words by frequency (most frequent words first)
            sorted_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
            
            # Display the sorted results
            print(f"\nWords related to the root '{word_root}' (sorted by popularity):")
            for word, freq in sorted_words:
                print(f"{word}: {freq} occurrences")

        else:
            print(f"\nNo words found related to the root '{word_root}'.")
    else:
        print("You must enter a word root.")

# Run the program
if __name__ == "__main__":
    main()

