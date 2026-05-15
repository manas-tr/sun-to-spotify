import re

from bs4 import BeautifulSoup


def clean_html(raw_html: str) -> str:

    soup = BeautifulSoup(raw_html, "html.parser")

    text = soup.get_text(separator=" ")

    noise_patterns = [
        r"Article URL:\s*\S+",
        r"Comments URL:\s*\S+",
        r"Points:\s*\d+",
        r"# Comments:\s*\d+",
    ]

    for pattern in noise_patterns:
        text = re.sub(pattern, "", text)

    cleaned_text = " ".join(text.split())

    return cleaned_text.strip()