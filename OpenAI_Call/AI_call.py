from http.client import responses

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=API_KEY,
)



responce = client.chat.completions.create(
    model = "deepseek/deepseek-r1:free",
    messages=[
        {"role": "user",
         "content":"What is the difference between Celsius and Fahrenheit ?"}
    ]
)

Answer = responce.choices[0].message.content

print(Answer.strip("\n").strip())
