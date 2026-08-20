from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1")

response = client.moderations.create(
    model="omni-moderation-latest",
    input="I want to hurt someone"
)


print(response.output_text)