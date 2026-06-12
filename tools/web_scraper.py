import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No Title"

        paragraphs = soup.find_all("p")

        content = "\n".join(
            p.get_text(strip=True)
            for p in paragraphs
        )

        return {
            "title": title,
            "content": content[:5000]
        }

    except Exception as e:
        return {"error": str(e)}