from tools.web_scraper import scrape_website
from ai.gemini_client import ask_ai


def summarize_website(url):

    data = scrape_website(url)

    if "error" in data:
        return data["error"]

    prompt = f"""
    Summarize the following website content.

    Title:
    {data['title']}

    Content:
    {data['content']}
    """

    return ask_ai(prompt)