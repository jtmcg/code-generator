import openai
from src.env import get_openai_pat

class GPT:
    def __init__(self, model):
        self.model = model
        self.client = openai.Client(api_key=get_openai_pat())
    
    def get_completion(self, prompt, temperature=0):
        messages = [{"role": "user", "content": prompt}]
        response = self.client.chat.completions.create(model=self.model, messages=messages, temperature=temperature)
        return response.choices[0].message.content