from google import genai
from webscrape import download_website, seperate_headers_paragraphs
import sys


def sentiment_analysis(content):
    with open("key.private") as handle:
        api_key = handle.read()

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=content,
        config=genai.types.GenerateContentConfig(
            system_instruction="Perform sentimental analysis on this scraped website. Give a short 3-5 sentence summary, a score from 0-10 (negative to positive), and answer the following questions. What led to you giving this article the score you gave it? What emotions are present in the article?")
    )
    print(response.text)


def main(url):
    website = download_website(url)
    content = seperate_headers_paragraphs(website)
    # print(str(content))
    sentiment_analysis(str(content))


if __name__ == "__main__":
    args = sys.argv
    if len(args) >= 2:
        main(args[1])
