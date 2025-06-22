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


# def ask_gpt4(user_input, chat_history=[]):
#     messages = [{"role": "system", "content": "You are an AI assistant helping with design thinking."}]
#     messages.extend(chat_history)
#     messages.append({"role": "user", "content": user_input})

#     try:
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=messages
#         )
    
#         return response.choices[0].message.content

#     except (RateLimitError, APIConnectionError, OpenAIError):
#         return "Sorry, the AI is currently unavailable. Please try again later."



#using llama
import requests
def ask_llama(user_input, chat_history=None):
    if chat_history is None:
        chat_history = []

    history_text = "You are an AI assistant helping with design thinking.\n"
    for message in chat_history:
        role = message["role"]
        content = message["content"]
        if role == "user":
            history_text += f"User: {content}\n"
        elif role == "assistant":
            history_text += f"AI: {content}\n"
    history_text += f"User: {user_input}\nAI:"

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": history_text,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json().get("response", "")
    except requests.exceptions.RequestException:
        return "Sorry, the local AI model is currently unavailable."
