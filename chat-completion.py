from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="VAR_chat_model_id",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello"}
    ]
)

print(completion.choices[0].message)