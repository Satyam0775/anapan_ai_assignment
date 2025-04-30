import requests
import pandas as pd
import time
import os

# ✅ Safely get the API key from environment or fallback
API_KEY = os.getenv("SERPAPI_API_KEY", "2734440723a44965d742e83a88d4563b88ed622648ae04d83f582eb7987fed71")

def get_collaboration_data(competitors, target="Virgin Media"):
    results = []

    for comp in competitors:
        query = f"{comp} {target} partnership OR collaboration"
        params = {
            "q": query,
            "api_key": API_KEY,
            "engine": "google",
            "num": 5
        }

        print(f"Searching: {query}")  # or use logging
        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()

        for item in data.get("organic_results", []):
            results.append({
                "Competitor": comp,
                "Title": item.get("title"),
                "Link": item.get("link"),
                "Snippet": item.get("snippet", "")
            })

        time.sleep(1)  # ✅ Respect API rate limits

    return pd.DataFrame(results)
