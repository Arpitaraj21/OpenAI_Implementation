from openai import OpenAI
import json

client = OpenAI()


#  define tool
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city"
                }
            },
            "required": ["city"]
        }
    }
]


# create actual function
def get_weather(city):
    return {
        "city": city,
        "temperature": 30,
        "condition": "Sunny"
    }
    

# send the user's question

response = client.responses.create(
    model="gpt-5.6",
    input="What's the weather in Hyderabad",
    tools=tools
)

print(response.output_text)

get_weather("Hyderabad")

print(result)

# Output
# [
#     ResponseFunctionToolCall(
#         call_id="call_abc123",
#         name="get_weather",
#         arguments='{"city":"Hyderabad"}',
#         type="function_call"
#     )
# ]

for item in response.output:
    if item.type == "function_call":
        print(item.name)
        print(item.arguments)
        
# expected output - get_weather
# {"city":"Hyderabad"}

# convert the arguments from JSON string -> Python dict
arguments = json.loads(item.arguments)
print(arguments)

# expected output  -> {"city": "Hyderabad"}


result = get_weather(arguments["city"])
print(result)

# response.output and response.output_text are two different things 
# for response.output_text -> Python is a high-level programming language...
# for response.output -> [
    # ResponseFunctionToolCall(
    #     type="function_call",
    #     name="get_weather",
    #     arguments='{"city":"Hyderabad"}',
    #     call_id="call_123"
    # )
# ]