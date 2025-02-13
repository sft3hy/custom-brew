from config import NEWS_API_KEY
import requests

def get_news(topic: str):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,             # Topic to search for
        "language": "en",       # Only fetch English articles
        "sortBy": "publishedAt",# Sort by most recent articles
        "pageSize": 10,         # Limit to 10 articles
        "apiKey": NEWS_API_KEY       # Your NewsAPI key
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        return [
            {
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "publishedAt": article["publishedAt"]
            }
            for article in articles
        ]
    else:
        return {"error": f"Failed to fetch articles. Status code: {response.status_code}"}