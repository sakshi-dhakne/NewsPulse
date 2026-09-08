def categorize_news(article):

    title = article.get("title") or ""
    description = article.get("description") or ""

    text = (title + " " + description).lower()

    technology_keywords = [
        "ai", "artificial intelligence", "technology",
        "software", "iphone", "android", "google",
        "microsoft", "apple", "amazon", "cybersecurity"
    ]

    sports_keywords = [
        "cricket", "football", "nfl", "nba",
        "sports", "soccer", "tennis", "baseball"
    ]

    business_keywords = [
        "stock", "finance", "market", "business",
        "economy", "investment", "company", "earnings"
    ]

    if any(keyword in text for keyword in technology_keywords):
        return "Technology"

    elif any(keyword in text for keyword in sports_keywords):
        return "Sports"

    elif any(keyword in text for keyword in business_keywords):
        return "Business"

    return "General"