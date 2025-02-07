from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

# Load a distilled model (e.g., DistilBERT)
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create a pipeline for sentiment analysis
nlp_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Run inference
text = "Hello, world! This is a distilled model in action."
result = nlp_pipeline(text)

print(result)  # [{'label': 'POSITIVE', 'score': 0.9998}]


