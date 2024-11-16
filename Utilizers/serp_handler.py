import os
from serpapi import GoogleSearch
from dotenv import load_dotenv


load_dotenv()

SERP_API_KEY = os.getenv("SERPAPI_KEY")

def search_entity_info(query):
    params = {
        "api_key": SERP_API_KEY,
        "engine": "google",
        "q": query,
        "google_domain": "google.co.in",
        "gl": "in",
        "hl": "en",
        "location": "India"
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()  
        return results
    except Exception as e:
        return {"error": f"Failed to retrieve search results: {str(e)}"}
