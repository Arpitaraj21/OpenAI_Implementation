from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": """Return the answer in JSON.
    
The JSON must contain:
- name: string
- age: number

Return ONLY valid JSON.

John is 25 years old."""
        }
    ]
)

# print(response.choices[0].message.content)

try:
    data = json.loads(response.output_text)
    print("Valid Json")
    print(data)
    
except json.JSONDecodeError:
    print("Invalid JSON returned by the model")