import requests
from operator import itemgetter

# Make an API call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("Status code: ", r.status_code)

# Process information about each submission
submission_ids = r.json()
submission_dicts = []


