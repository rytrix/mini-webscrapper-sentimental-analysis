from google import genai
from webscrape import download_website, seperate_headers_paragraphs
import sys
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

def sentiment_analysis(content):
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=content,
        config=genai.types.GenerateContentConfig(
            system_instruction="Perform sentimental analysis on this scraped website. Give a short 3-5 sentence summary, a score from 0-10 (negative to positive), and answer the following questions. What led to you giving this article the score you gave it? What emotions are present in the article?")
    )
    return response.text


def download_and_analyze(url):
    website = download_website(url)
    content = seperate_headers_paragraphs(website)
    # print(str(content))
    analysis = sentiment_analysis(str(content))
    return analysis


if __name__ == "__main__":
    args = sys.argv
    if len(args) >= 2:
        print(download_and_analyze(args[1]))
