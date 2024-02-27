import os

def get_openai_pat():
    return os.getenv("OPENAI_API_KEY")