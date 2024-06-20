import os
from openai import OpenAI


# Function to chat with GPT-3.5-turbo
def chat_with_gpt(prompt):
    client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content

# Example usage
user_input = "Hello, how can I use OpenAI's API? answer in 10 words"
response = chat_with_gpt(user_input)
print(response)


