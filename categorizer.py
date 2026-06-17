def categorize_news(title):

    title = title.lower()

    if any(word in title for word in ["election", "government", "minister", "parliament"]):
        return "Politics"

    elif any(word in title for word in ["ai", "artificial intelligence", "chatgpt", "openai"]):
        return "AI"

    elif any(word in title for word in ["match", "football", "cricket", "sports"]):
        return "Sports"

    elif any(word in title for word in ["accident", "crash", "murder", "crime"]):
        return "Accident/Crime"

    else:
        return "General"