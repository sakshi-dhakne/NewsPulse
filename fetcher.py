import feedparser


def get_news():

    feeds = {
        "BBC": "https://feeds.bbci.co.uk/news/rss.xml",
        "CNN": "http://rss.cnn.com/rss/edition.rss",
        "NYTimes": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    }

    all_news = []

    for source, url in feeds.items():

        feed = feedparser.parse(url)

        for article in feed.entries[:10]:

            all_news.append({
                "source": source,
                "title": article.title,
                "link": article.link
            })

    return all_news