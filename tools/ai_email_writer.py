from ai.gemini_client import ask_ai
from ai.prompts import EMAIL_PROMPT

def generate_email(topic):
    prompt = EMAIL_PROMPT.format(topic)

    return ask_ai(prompt)