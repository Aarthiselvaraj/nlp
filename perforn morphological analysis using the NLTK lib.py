import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag



def perform_morphological_analysis(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Perform part-of-speech tagging
    pos_tags = pos_tag(words)

    return pos_tags

# Example usage
def main():
    text = "The quick brown fox jumps over the lazy dog."

    # Perform morphological analysis
    analysis_result = perform_morphological_analysis(text)

    # Display the result
    print("Original Text:", text)
    print("\nMorphological Analysis:")
    for word, pos_tag in analysis_result:
        print(f"{word}: {pos_tag}")

if __name__ == "__main__":
    main()
