def categorize_news(article):

    text = (
        article.get("title", "") +
        " " +
        article.get("description", "")
    ).lower()

    if any(word in text for word in ["ai", "technology", "software"]):
        return "Technology"

    elif any(word in text for word in ["cricket", "football", "sports"]):
        return "Sports"

    elif any(word in text for word in ["stock", "finance", "market"]):
        return "Business"

    return "General"


def get_summary(article):

    return article.get("description", "No summary available")