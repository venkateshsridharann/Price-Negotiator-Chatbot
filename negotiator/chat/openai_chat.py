import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Function to chat with GPT-3.5-turbo
def chat_with_gpt(prompt,all_messages):
    context = '\n--'.join(['{}:{}'.format(x.sender,x.content) for x in all_messages])
    client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
    
    prompt = '--continue this chat based on the previous chat. \n CONTEXT \n{}\n --respond in ten words to the following prompt {}'.format(context,prompt)
    print(prompt)
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



