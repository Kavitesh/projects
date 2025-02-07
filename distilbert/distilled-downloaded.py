import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load the model and tokenizer from local files
model_path = "distilbert-base-uncased-finetuned-sst-2-english"  # Update this to your actual path
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True, use_fast=False)
model = AutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True, from_tf=False) # make from_tf true if no dedicated GPU

# Function to get sentiment prediction
def classify_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    predicted_class = torch.argmax(probabilities).item()
    
    return "Positive" if predicted_class == 1 else "Negative"

# Example usage
print(classify_text("I love this movie!"))  # Expected: Positive
print(classify_text("This is the worst experience ever."))  # Expected: Negative
