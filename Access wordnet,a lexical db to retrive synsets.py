from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')

def get_synsets(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets
    else:
        return f"No synsets found for {word}"

def explore_synset(synset):
    print(f"Synset: {synset.name()}")
    print(f"Definition: {synset.definition()}")
    print(f"Examples: {synset.examples()}")
    print()

def main():
    word = input("Enter a word to explore: ")
    synsets = get_synsets(word)

    if isinstance(synsets, str):
        print(synsets)
    else:
        for synset in synsets:
            explore_synset(synset)

if __name__ == "__main__":
    main()
