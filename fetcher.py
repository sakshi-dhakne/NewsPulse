import requests

def fetch_news(api_key):

    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"country=us&pageSize=20&apiKey={api_key}"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return data.get("articles", [])
        
        print("Failed to fetch news:", response.status_code)
        return []

    except requests.exceptions.RequestException as error:
        print("Error:", error)
        return []
    