import os
import requests
from dotenv import load_dotenv

load_dotenv()


def generate_x_post(user_input: str) -> str:

    prompt= f""" 
    You are a social media expert.
    You are given a user input and you need to generate a post for x.
    The post should be in the following format:
    <topic>
    {user_input}
    </topic>
    """

    payload = {
        "model": "gpt-4o",
        "input": prompt,
    }
    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
            "Content-Type": "application/json",
        },
        json=payload
    )
    response_text = response.json().get("output", [{}])[0].get("content",[{}])[0].get("text","")
    return response_text

def main():    
    user_input = input("What should the post be about? ")
    x_post = generate_x_post(user_input)
    print("x_post: ", x_post)



if __name__ == "__main__":
    main()
