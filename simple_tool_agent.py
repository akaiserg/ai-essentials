import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_temperature(city: str) -> float:
    """
    Get the temperature for a given city
    """
    return 20.0

def get_prompt(user_input: str) -> str:
    return f"""
    You are a helpful assistant that can help. Response in a kind and helpful way.
    
    You can also use tools to get the temperature of a city.
    - get_temperature(city: str) -> float: Get the temperature for a given city

    if you need to use a tool, use the following format: tool_name: arg1, arg2, arg3.

    For example:
    get_temperature: Paris

    with that in mind, here is the user input:
    <user-question>
    {user_input}
    </user-question>

    if you request a tool, plese output ONLY the tool name and the arguments.
    """

def main():
    user_input = input("Enter a city: ")
    temperature = get_temperature(user_input)
    response = client.responses.create(
        model="gpt-4o",
        input=get_prompt(user_input),
    )
    reply = response.output_text
    print(reply)   
    if reply.startswith("get_temperature"):
        tool_name, args = reply.split(":")
        args = args.split(",")
        print(tool_name, args)
        temperature = get_temperature(args[0])
        print(f"The temperature in {args[0]} is {temperature}°C")
        second_prompt = f"""
        You are a helpful assistant that can help. Response in a kind and helpful way.
        
        You requested the temperature for {args[0]}.
        This is the temperature given by the tool: {temperature}        
        """
        second_response = client.responses.create(
            model="gpt-4o",
            input=second_prompt,
        )
        second_reply = second_response.output_text
        print(second_reply)
    else:
        print(reply)



if __name__ == "__main__":
    main()
