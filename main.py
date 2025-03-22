from bs4 import BeautifulSoup
import requests


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

def main():
    website = download_website("https://www.coindesk.com/markets/2025/03/17/crypto-whale-shorts-usd445m-in-btc-while-taking-bullish-bet-on-melania-token-hyperliquid-data-show")
    content = seperate_headers_paragraphs(website)
    print(content)
    

main()
