from transformers import MarianMTModel, MarianTokenizer

def translate_text(input_text, model, tokenizer, source_lang='en', target_lang='fr'):
    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Translate the input text
    translation_ids = model.generate(input_ids, max_length=100, num_beams=4, no_repeat_ngram_size=2, top_k=50, top_p=0.95, length_penalty=0.6)

    # Decode the translated text
    translated_text = tokenizer.decode(translation_ids[0], skip_special_tokens=True)
    
    return translated_text

# Load pre-trained model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-fr"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Example usage
english_text = "Hello, how are you?"
translated_text = translate_text(english_text, model, tokenizer)

print(f"English: {english_text}")
print(f"French: {translated_text}")
