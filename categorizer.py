def categorize_news(title):

    title = title.lower()

    politics_words = [
        "government",
        "president",
        "minister",
        "election",
        "parliament"
    ]

    ai_words = [
        "ai",
        "artificial intelligence",
        "openai",
        "chatgpt",
        "gemini"
    ]

    sports_words = [
        "cricket",
        "football",
        "tennis",
        "match",
        "sports"
    ]

    accident_words = [
        "accident",
        "crash",
        "murder",
        "crime",
        "death",
        "killed"
    ]

    if any(word in title for word in politics_words):
        return "Politics"

    elif any(word in title for word in ai_words):
        return "AI"

    elif any(word in title for word in sports_words):
        return "Sports"

    elif any(word in title for word in accident_words):
        return "Accident/Crime"

    else:
        return "General"