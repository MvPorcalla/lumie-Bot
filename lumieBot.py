import os
import random
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables (useful for local testing; GitHub Actions injects them automatically)
load_dotenv()

# Get PAGE_ID and PAGE_ACCESS_TOKEN from environment variables
PAGE_ID = os.getenv("LUMIE_PAGE_ID")
PAGE_ACCESS_TOKEN = os.getenv("LUMIE_PAGE_ACCESS_TOKEN")

# Validate environment variables
if not PAGE_ID or not PAGE_ACCESS_TOKEN:
    raise ValueError("PAGE_ID and PAGE_ACCESS_TOKEN must be set in environment variables or GitHub secrets.")

# Load quotes from quotes.txt
try:
    with open("quotes.txt", "r", encoding="utf-8") as file:
        quotes = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    raise FileNotFoundError("quotes.txt not found in project directory.")

# Randomly select a quote
quote = random.choice(quotes)

# Format the Facebook post
today = datetime.now().strftime("%B %d, %Y")
POST_TEMPLATE = (
    f"🌟 Quote of the Day 🌟\n\n"
    f"\"{quote}\"\n\n"
    f"—\n"
    f"🤖 Posted by LumieBot • 📅 {today}\n"
    f"#LumieBot #Motivation #Mindset #WordsWithoutWarning #BuiltWithPython"
)

# Prepare the API request
url = f"https://graph.facebook.com/{PAGE_ID}/feed"
payload = {
    "message": POST_TEMPLATE,
    "access_token": PAGE_ACCESS_TOKEN
}

# Make the POST request
response = requests.post(url, data=payload)

# Handle the response
if response.status_code == 200:
    print("✅ Successfully posted to Facebook.")
    print("📌 Message:\n", POST_TEMPLATE)
else:
    print("❌ Failed to post to Facebook.")
    print("Status Code:", response.status_code)
    print("Response:", response.json())
