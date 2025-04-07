from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
from browser_use import Agent
from dotenv import load_dotenv
import os
import re
import json
load_dotenv()

import asyncio

api_key = os.getenv("GEMINI_API_KEY")
# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))


async def main():
    agent = Agent(
        task="Obtain a list of 5 full crypto news article urls from cointelegraph to perform sentiment analysis on in a json format inside brackets like this [\"url\", \"url\", \"url\", \"url\", \"url\"], do not visit the urls, and do not extract the full text from the urls.",
        llm=llm,
    )
    result = await agent.run()
    print(result.final_result())

    match = re.search(r'\[.*?\]', result.final_result())
    data = match.group(0) if match else None  # Set json to the matched text or None if no match
    print(data)

    json_data = json.loads(data) if data else None  # Load the JSON data if it was found
    print(json_data)


    analysis = []
    for i in json_data:
        print(i)
        from main import download_and_analyze
        try:
            analysis.append(f"url: {i}\n" + download_and_analyze(i))
        except:
            print(f"Error processing URL: {i}")
            continue
    
    with open("analysis.md", "w") as f:
        for i in analysis:
            f.write(i + "\n")


    


if __name__ == "__main__":
    asyncio.run(main())
    
# print("Hello?")





