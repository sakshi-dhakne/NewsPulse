from fetcher import get_news
from categorizer import categorize_news

news = get_news()

for article in news:
    category = categorize_news(article["title"])

    print(f"Category: {category}")
    print(article["title"])
    print(article["source"])
    print(article["title"])
    print(article["link"])
    print("-" * 50)
