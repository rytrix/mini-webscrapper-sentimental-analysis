from bs4 import BeautifulSoup
import requests
import sys


def download_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.3"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None


def seperate_headers_paragraphs(website):
    soup = BeautifulSoup(website, "html.parser")

    extracted_text = []

    for tag in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "span", "a", "li"]):
        extracted_text.append(tag.get_text(strip=True))

    return extracted_text


def main(url):
    website = download_website(url)
    content = seperate_headers_paragraphs(website)
    print(content)


if __name__ == "__main__":
    args = sys.argv
    if len(args) >= 2:
        main(args[1])
