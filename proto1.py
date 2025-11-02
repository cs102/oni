import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Initialize the stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Function to split the word into prefix, root, and suffix using NLTK
def split_word_with_nltk(word):
    # Tokenize the word
    tokens = word_tokenize(word)

    # Lemmatize to get the root word
    lemmatized_word = lemmatizer.lemmatize(tokens[0])

    # Stem to get the stemmed word
    stemmed_word = stemmer.stem(tokens[0])

    # POS tagging to identify the part of speech
    pos_tags = nltk.pos_tag(tokens)
    
    # Output the results
    print(f"Original Word: {word}")
    print(f"Lemmatized Word (Root): {lemmatized_word}")
    print(f"Stemmed Word (Root): {stemmed_word}")
    print(f"POS Tags: {pos_tags}")

# Example usage
word = input("Enter a word: ").strip().lower()
split_word_with_nltk(word)

