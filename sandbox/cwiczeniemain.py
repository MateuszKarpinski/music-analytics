import requests
import time
import os
from dotenv import load_dotenv

url = 'https://musicbrainz.org/ws/2/artist/'

params = {
    'query' : 'tag:pop',
    'limit' : 10,
    'fmt' : 'json'
}

header = {
    'User-Agent' : os.getenv('MB_USER_AGENT')
}

r = requests.get(url, params=params, headers=header)

dane = r.json()

for i, artist in enumerate(dane['artists'], start=1) :
    print(f"{i}. {artist['name']}")
    time.sleep(1)


