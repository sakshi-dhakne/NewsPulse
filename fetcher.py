import feedparser

def get_news():
    news_list = []

    feeds = {
        "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
        "Reuters": "https://feeds.reuters.com/reuters/topNews",
        "CNN": "http://rss.cnn.com/rss/edition.rss"
    }

    for source, url in feeds.items():
        feed = feedparser.parse(url)

        for article in feed.entries[:5]:
            news_list.append({
                "source": source,
                "title": article.title,
                "link": article.link
            })

    return news_list