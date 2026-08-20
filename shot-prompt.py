from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.6",
    instructions="""
    Classify the user's message as either "question" or "statement".
    
    Example input:
    What is Python?
    
    Example output:
    question
    
    Now classify the user's message.
    """,
    
    input="Can you explain APIs?"
)


print(response.output_text)