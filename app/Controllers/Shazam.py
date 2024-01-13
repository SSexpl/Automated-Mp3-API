import requests
from dotenv import load_dotenv
import os

# # Load environment variables from .env file
# load_dotenv()

# # Get the API key from the environment variables
# shazam_api_key = os.getenv("RAPIDAPI_KEY")

# # Ensure the API key is present
# if not shazam_api_key:
#     raise ValueError("API key is missing in the .env file.")

# url = "https://shazam.p.rapidapi.com/search"
# title = "Hey Jude"
# artist = "The Beatles"
# querystring = {"term": title, "locale": "en-US", "offset": "0", "limit": "1"}

# headers = {
#     "X-RapidAPI-Key": shazam_api_key,
#     "X-RapidAPI-Host": "shazam.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())
