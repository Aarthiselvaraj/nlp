from nltk.stem import PorterStemmer

def perform_stemming(words):
    # Initialize the Porter Stemmer
    porter_stemmer = PorterStemmer()

    # Apply stemming to each word in the list
    stemmed_words = [porter_stemmer.stem(word) for word in words]

    return stemmed_words

# Example usage
def main():
    words = ["running", "easily", "happily", "better", "cats", "dogs", "jumping"]

    # Perform stemming
    stemmed_words = perform_stemming(words)

    # Display the result
    for original, stemmed in zip(words, stemmed_words):
        print(f"Original: {original}, Stemmed: {stemmed}")

if __name__ == "__main__":
    main()
