from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer from the local directory
tokenizer = AutoTokenizer.from_pretrained("./deepseek-r1-distill-qwen-1-5b")
model = AutoModelForCausalLM.from_pretrained("./deepseek-r1-distill-qwen-1-5b")

input_text = "Write a Python function to calculate the sum of two numbers."

# Tokenize the input
inputs = tokenizer(input_text, return_tensors="pt")

# Generate text
outputs = model.generate(**inputs, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.pad_token_id )

# Decode the generated text
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)