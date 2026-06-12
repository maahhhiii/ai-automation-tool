from ai.gemini_client import ask_ai
from ai.prompts import RESUME_PROMPT

def analyze_resume(resume_text):
    prompt = RESUME_PROMPT.format(resume_text)

    return ask_ai(prompt)