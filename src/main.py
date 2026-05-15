import os
import time
import requests
from dotenv import load_dotenv
load_dotenv()
url = "https://musicbrainz.org/ws/2/artist/"
params = {
    'query' : 'tag:rock',
    'limit' : 5,
    'fmt' : 'json'
}
headers = {
    'User-Agent' : os.getenv('MB_USER_AGENT')
}
r = requests.get(url, params=params, headers=headers)

data = r.json()
for i, artist in enumerate(data['artists'], start=1):
    print(f"{i}. {artist['name']}")



print(r.status_code)
print(r.request.headers.get('User-Agent'))

time.sleep(1)