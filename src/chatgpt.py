from src.prompt import Prompt

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = os.getenv("OPENAI_MODEL", default = "gpt-3.5-turbo")
        #self.model = os.getenv("OPENAI_MODEL", default = "chatbot")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0))
        self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 240))

    def get_response(self):
        response = openai.ChatCompletion.create(
        model = model_id,
        messages = conversation_string
        )
        api_usage = response['usage']
        #print(api_usage)
        #print(str(response))
        conversation_string.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation[-1]['content'].strip()

    def add_msg(self, text):
        self.prompt.add_msg(text)
