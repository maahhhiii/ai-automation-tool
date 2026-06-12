import re
from collections import Counter


def analyze_file(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        lines = text.splitlines()
        words = text.split()

        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, text)

        word_frequency = Counter(words)
        common_words = word_frequency.most_common(5)

        report = {
            "Lines": len(lines),
            "Words": len(words),
            "Characters": len(text),
            "Emails Found": emails,
            "Top 5 Words": common_words
        }

        return report

    except Exception as e:
        return f"Error: {e}"