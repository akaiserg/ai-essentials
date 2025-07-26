import os
from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def execute_tool(tool_call) -> str:
    """
    Execute a tool call
    """
    fn_name = tool_call.function.name
    fn_args = json.loads(tool_call.function.arguments)
    if fn_name in available_tools:
        try:
            return available_tools[fn_name](**fn_args)
        except Exception as e:
            return f"Error executing tool {fn_name}: {e}"
    else:
        return f"Tool {fn_name} not found"


def get_temperature(city: str) -> float:
    """
    Get the temperature for a given city
    """
    return 20.0

available_tools = {
    "get_temperature": get_temperature,
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_temperature",
            "description": "Get the temperature for a given city",
            "parameters": {
                "type": "object", 
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to get the temperature for"
                    }
                },
                "additionalProperties": False,
                "required": ["city"],
            },
        }
    },
]

def main():
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that can help. Respond in a kind and helpful way.",
        }
    ]
    
    while True:
        user_input = input("Enter your question: ")
        if user_input == "exit":
            break
            
        messages.append({
            "role": "user",
            "content": user_input,
        })
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )
        
        message = response.choices[0].message
        messages.append(message)
        
        # Check if the model wants to call a tool
        if message.tool_calls:
            # Execute each tool call
            for tool_call in message.tool_calls:
                tool_output = execute_tool(tool_call)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(tool_output),
                })
            
            # Get the final response after tool execution
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
            )
            print(response.choices[0].message.content)
        else:
            print(message.content)


if __name__ == "__main__":
    main()
