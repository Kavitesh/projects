# set env variable OPENAI_API_KEY 
from openai import OpenAI
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "Hello World"}
    ]
)
