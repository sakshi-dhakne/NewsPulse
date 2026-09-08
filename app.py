from fetcher import fetch_news
from analyzer import categorize_news
from email_sender import send_email

from config import (
    NEWS_API_KEY,
    EMAIL,
    EMAIL_PASSWORD,
    RECEIVER_EMAIL
)

articles = fetch_news(NEWS_API_KEY)

if not articles:
    print("No news articles found. Exiting.")
    exit()

digest = ""

for article in articles[:15]:

    category = categorize_news(article)

    digest += (
    f"\n[{category}]\n"
    f"{article.get('title', 'No Title')}\n"
    f"{article.get('url', 'No URL')}\n\n"
    )

send_email(
    EMAIL,
    EMAIL_PASSWORD,
    RECEIVER_EMAIL,
    digest
)

print("Articles fetched:", len(articles))