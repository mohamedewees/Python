from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

chat_log = []

while True:
    user_messages = input()
    if user_messages.lower() == "quit":
        break
    else:
        chat_log.append({"role":"user", "content":user_messages})
        response = client.chat.completions.create(
            model = "deepseek/deepseek-r1:free",
            messages = chat_log
        )
        assistant_response = response.choices[0].message.content
        print("DeepSeek: " + assistant_response.strip("\n").strip())
        chat_log.append({"role":"assistant", "content": assistant_response.strip("\n").strip()})

#what is the difference between interpreted and compiled languages ?