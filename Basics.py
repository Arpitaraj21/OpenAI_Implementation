# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# import time

# load_dotenv() 

# client = OpenAI(
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     base_url="https://openrouter.ai/api/v1"
# )

# start = time.time()

# response = client.responses.create(
#     model='gpt-5.6',
#     input="Write a story for bedtime about unicorn",
#     temperature=0.5,
#     max_output_token=20,
#     stream=True
# )


# #  system level instruction

# # response = client.responses.create(
# #     model="YOUR_MODEL",
# #     instructions="You are a Python tutor. Explain concepts to complete beginners using simple examples.",
# #     input="Explain recursion",
# #     stream=True
# # )

# # events we receive
# for event in stream:
#     print(event)

# # only the text as it arrives
# for event in stream:
#     if event.type == "reponse.output_text.delta":
#         print(event.delta, end="", flush=True)
    
# end = time.time()

# print(response)
# print(response.id)
# print(response.model)
# print(response.usage)   # token usage 
# print(response.output_text)


# # by the time we can check the latency of different models

from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

start = time.time()

response = client.responses.create(
    model="openai/gpt-5.5",
    input="Write a short bedtime story about a unicorn",
    temperature=0.5,
    max_output_tokens=100
)

# print(response.output)

end = time.time()

print("\nLatency:", end - start, "seconds")

# log token usage
print("\nUsage:")
print(response.usage)


print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("Total tokens:", response.usage.total_tokens)
print("Cost:", response.usage.cost)