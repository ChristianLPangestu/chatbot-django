from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def ask_gpt4(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant helping with design thinking."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content
