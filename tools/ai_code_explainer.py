from ai.gemini_client import ask_ai
from ai.prompts import CODE_PROMPT

def explain_code(code):
    prompt = CODE_PROMPT.format(code)

    return ask_ai(prompt)