from ai.gemini_client import ask_ai

def summarize_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        prompt = f"Summarize the following text:\n\n{text}"

        return ask_ai(prompt)

    except FileNotFoundError:
        return "Error: File not found."

    except PermissionError:
        return "Error: Please provide a file path, not a folder path."

    except Exception as e:
        return f"Error: {e}"