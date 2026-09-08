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

    politics_keywords = [
    "election", "government", "president", "senate",
    "congress", "parliament", "minister", "policy",
    "vote", "political"
    ]

    crime_keywords = [
    "crime", "murder", "arrest", "police",
    "shooting", "robbery", "theft", "fraud",
    "assault", "investigation"
    ]

    if any(keyword in text for keyword in technology_keywords):
        return "Technology"

    elif any(keyword in text for keyword in sports_keywords):
        return "Sports"

    elif any(keyword in text for keyword in business_keywords):
        return "Business"

    elif any(keyword in text for keyword in politics_keywords):
        return "Politics"
    elif any(keyword in text for keyword in crime_keywords):
        return "Crime"

    return "General"