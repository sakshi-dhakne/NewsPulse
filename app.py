from fetcher import fetch_news
from analyzer import categorize_news,get_summary
from email_sender import send_email

from config import (
    NEWS_API_KEY,
    EMAIL,
    EMAIL_PASSWORD,
    RECEIVER_EMAIL
)

import fetcher

fetcher.API_KEY = NEWS_API_KEY

articles = fetch_news()

result = ""

for article in articles[:15]:

    category = categorize_news(article)

    result += (
        f"\n[{category}]\n"
        f"{article['title']}\n"
        f"{article['url']}\n\n"
    )

send_email(
    EMAIL,
    EMAIL_PASSWORD,
    RECEIVER_EMAIL,
    result
)

