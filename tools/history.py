import os
from datetime import datetime


def save_history(feature_name, content):

    os.makedirs("data/history", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"data/history/{feature_name}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    return filename