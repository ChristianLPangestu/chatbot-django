import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY
from openai import OpenAIError
from openai._exceptions import RateLimitError, APIConnectionError

def ask_gpt4(user_input, chat_history=None, model="gpt-4o"):
    if chat_history is None:
        chat_history = []

    messages = [{"role": "system", "content": "You are an AI assistant helping with design thinking."}]
    messages.extend(chat_history)
    messages.append({"role": "user", "content": user_input})

    try:
        response = openai.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content

    except RateLimitError:
        return "You're sending requests too quickly. Please wait a moment."
    except APIConnectionError:
        return "Cannot connect to OpenAI server. Please check your network."
    except OpenAIError as e:
        return f"OpenAI error: {str(e)}"