from openai import OpenAI, RateLimitError, BadRequestError
import time
import json

client = OpenAI(timeout=10.0)

max_retries = 4

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
            }
        }
    }
]

def get_weather(city):
    return {
        "city": city,
        "temperature": 30,
        "condition": "Sunny"
    }
    
for attempt in range(max_retries):
    try:
        response = client.responses.create(
        model='gpt-5.6',
        input="What's the weather in Hyderabad",
        tools=tools
        )
        print(response.output_text)
        break
    
    except RateLimitError as e:
        if attempt == max_retries - 1:
            print("Failed after all retries")
            raise
        
        delay = 2 ** attempt
        
        print(f"Rate limit. Retrying in {delay} seconds")
        time.sleep(delay)
        
    # except BadRequestError as e:
    #     print("Invalid request", e)
    

for item in response.output:
    if item.type == "function_call":
        print("function:", item.name)
        print("arguments:", item.arguments)
        arguments = json.loads(item.arguments)
        result = get_weather(arguments["city"])
        print("tool results", result)
        print(response.usage)
        # when we do -> expected output -> ResponseUsage(
        # input_tokens=12,
        # output_tokens=18,
        # total_tokens=30
        # )
            
