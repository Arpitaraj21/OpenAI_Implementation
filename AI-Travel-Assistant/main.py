from openai import OpenAI
from dotenv import load_dotenv
from tools import get_weather, tools
import os
import json
import time

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    timeout=30.0
)

with open("conversation.json", "r") as file:
    conversation = json.load(file)


while True:

    user_input = input("You: ")

    if user_input.lower().strip() == "exit":
        break

    # -------------------------
    # 1. Add user message
    # -------------------------

    conversation.append({
        "role": "user",
        "content": user_input
    })

    # -------------------------
    # 2. First streamed request
    # -------------------------

    stream = None
    max_retries = 3

    for attempt in range(max_retries):

        try:

            stream = client.responses.create(
                model="gpt-5.6",
                input=conversation,
                max_output_tokens=100,
                stream=True,
                tools=tools
            )

            break

        except Exception as e:

            print(f"Attempt {attempt + 1} failed: {e}")

            if attempt < max_retries - 1:
                print("Retrying in 2 seconds...")
                time.sleep(2)

    if stream is None:
        print("Request failed after 3 attempts.")
        continue

    # -------------------------
    # 3. Read streamed response
    # -------------------------

    assistant_response = ""
    tool_call = None

    print("assistant: ", end="")

    for event in stream:

        # Uncomment this if you want to see events
        # print("\nEvent:", event.type)

        if event.type == "response.output_text.delta":

            print(event.delta, end="", flush=True)

            assistant_response += event.delta

        elif event.type == "response.completed":

            for item in event.response.output:

                if item.type == "function_call":

                    tool_call = item

    print()

    # -------------------------
    # 4. Handle tool call
    # -------------------------

    if tool_call:

        print("Tool call:", tool_call)

        arguments = json.loads(tool_call.arguments)

        city = arguments["city"]

        result = get_weather(city)

        print("Tool result:", result)

        # IMPORTANT:
        # Preserve the function call itself
        conversation.append({
            "type": "function_call",
            "id": tool_call.id,
            "call_id": tool_call.call_id,
            "name": tool_call.name,
            "arguments": tool_call.arguments
        })

        # IMPORTANT:
        # Send the tool result
        conversation.append({
            "type": "function_call_output",
            "call_id": tool_call.call_id,
            "output": json.dumps(result)
        })

        # -------------------------
        # 5. Ask model for final answer
        # -------------------------

        final_stream = client.responses.create(
            model="gpt-5.6",
            input=conversation,
            max_output_tokens=100,
            stream=True,
            tools=tools
        )

        final_response = ""

        print("assistant: ", end="")

        for event in final_stream:

            if event.type == "response.output_text.delta":

                print(event.delta, end="", flush=True)

                final_response += event.delta

        print()

        # Save final assistant answer
        conversation.append({
            "role": "assistant",
            "content": final_response
        })

    else:

        # -------------------------
        # 6. Normal response
        # -------------------------

        conversation.append({
            "role": "assistant",
            "content": assistant_response
        })

    # -------------------------
    # 7. Save conversation
    # -------------------------

    with open("conversation.json", "w") as file:
        json.dump(conversation, file, indent=4)