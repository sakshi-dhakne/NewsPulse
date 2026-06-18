from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

EMAIL = os.getenv("EMAIL")

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")