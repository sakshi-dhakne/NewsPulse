from fetcher import get_news
from categorizer import categorize_news
from email_sender import send_email


news = get_news()

categorized_news = {
    "Politics": [],
    "AI": [],
    "Sports": [],
    "Accident/Crime": [],
    "General": []
}


for article in news:

    category = categorize_news(article["title"])

    categorized_news[category].append(article)


email_content = "NEWSPULSE DAILY DIGEST\n\n"


for category, articles in categorized_news.items():

    email_content += f"\n{'=' * 40}\n"

    email_content += f"{category.upper()}\n"

    email_content += f"{'=' * 40}\n\n"

    for article in articles[:5]:

        email_content += f"• {article['title']}\n"

        email_content += f"{article['link']}\n\n"


print(email_content)

send_email(email_content)


