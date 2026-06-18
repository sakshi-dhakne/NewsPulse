def categorize_news(article):

    title = article.get("title") or ""
    description = article.get("description") or ""

    text = (title + " " + description).lower()

    if any(word in text for word in ["ai", "technology", "software"]):
        return "Technology"

    elif any(word in text for word in ["cricket", "football", "sports"]):
        return "Sports"

    elif any(word in text for word in ["stock", "finance", "market"]):
        return "Business"

    return "General"