import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{os.environ.get("ACCOUNT_ID")}/ai/run/"
headers = {"Authorization": f"Bearer {os.environ.get("API_TOKEN")}"}

def call(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()


# example
if __name__ == "__main__":
    inputs = [
        { "role": "system", "content": "You are a friendly assistan that helps write stories" },
        { "role": "user", "content": "Write a short story about a llama that goes on a journey to find an orange cloud in japanese"}
    ];
    output = call("@cf/meta/llama-3.3-70b-instruct-fp8-fast", inputs)
    print(output)
    print(output["result"]["responcse"])
