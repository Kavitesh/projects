from mitmproxy import http
import datetime
import json
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
    print(outputs)
    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    predicted_class = torch.argmax(probabilities).item()
    
    return "Positive" if predicted_class == 1 else "Negative"


# Log file to store request and response details
LOG_FILE = "http_traffic.log"

# Function to log data
def log_message(message: str):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

# Check request sent by user
def request(flow: http.HTTPFlow) -> None:
    request_details = (
        f"REQUEST:\n"
        f"URL: {flow.request.pretty_url}\n"
        f"Method: {flow.request.method}\n"
        f"Headers: {dict(flow.request.headers)}\n"
        f"Body: {flow.request.text}\n"
        "-----------------------\n"
    )
    log_message(request_details)

    # Check sentiment
    if classify_text(flow.request.text) == "Negative":
        flow.request.text = "blocked"
        log_message(f"Modified request to {flow.request.pretty_url}")    
    # Remove GDPR data
        
    # Rephrase using another agent
        


# Check response recieved from ai
def response(flow: http.HTTPFlow) -> None:
    response_details = (
        f"RESPONSE:\n"
        f"URL: {flow.request.pretty_url}\n"
        f"Status Code: {flow.response.status_code}\n"
        f"Headers: {dict(flow.response.headers)}\n"
        f"Body: {flow.response.text}\n"
        "-----------------------\n"
    )
    log_message(response_details)
    print(flow.request.text)
    print(flow.response.text)
    # Check classification of response body
    if classify_text(flow.response.text) == "Negative":
        try:
            data = json.loads(flow.response.text)
            data["received_from_ai"] = "blocked"
            flow.response.text = json.dumps(data)
        except json.JSONDecodeError:
            #flow.response.text = "BLOCKED"
        log_message(f"Modified response for {flow.request.pretty_url}")

