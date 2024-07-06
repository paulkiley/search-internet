import requests

def duckduckgo_search(query):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url)
    return response.json()

query = "example search"
results = duckduckgo_search(query)

for result in results['RelatedTopics']:
    print(f"Title: {result['Text']}")
    print(f"Link: {result['FirstURL']}")
    print()

