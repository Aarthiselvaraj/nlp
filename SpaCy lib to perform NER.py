import spacy

def perform_ner(text):
    
    nlp = spacy.load("en_core_web_sm")

    
    doc = nlp(text)

    
    print("Named Entities:")
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})")



def main():
    text = "Apple Inc. is planning to open a new store in New York City in 2022."

    
    perform_ner(text)

if __name__ == "__main__":
    main()
