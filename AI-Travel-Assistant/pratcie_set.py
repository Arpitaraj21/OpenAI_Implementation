# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# import json

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     base_url="https://openrouter.ai/api/v1"
# )

# with open("conversation.json", "r") as file:
#     conversation = json.load(file)
    
# while True:
#     user_input = input("You: ")
    
#     if user_input == "exit":
#         break
    
#     # for list
#     conversation.append({
#         "role": "user",
#         "content": user_input
#     })
    
        
#     response = client.responses.create(
#         model="gpt-5.6",
#         input=user_input,
#         max_output_tokens=20
#     )

#     print("Assistant: ", response.output_text)
    
#     # for list
#     conversation.append({
#         "role": "assistant",
#         "content": response.output_text
#     })
    
#     with open("conversation.json", "w") as file:
# 
# 
# json.dump(conversation, file, indent=4)

