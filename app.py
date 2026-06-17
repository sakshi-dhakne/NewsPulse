from fetcher import get_news

news = get_news()

for article in news:
    print(article["source"])
    print(article["title"])
    print(article["link"])
    print("-" * 50)