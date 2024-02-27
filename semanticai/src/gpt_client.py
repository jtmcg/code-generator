import openai
from src.env import get_openai_pat


class GPT:
    def __init__(self, model, temperature=0):
        self.model = model
        self.client = openai.Client(api_key=get_openai_pat())
        if temperature >=0 and temperature <= 1: self.temperature = temperature
    
    def get_completion(self, prompt):
        messages = [{"role": "user", "content": prompt}]
        response_format = {"type": "json_object"}
        response = self.client.chat.completions.create(model=self.model, messages=messages, response_format=response_format, temperature=self.temperature)
        return response.choices[0].message.content