import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()
USER_AGENT = os.getenv("MB_USER_AGENT")
BASE_URL = "https://musicbrainz.org/ws/2/artist/"

def fetch_artist(tag: str, limit: int, offset: int) -> dict:
    params = {
        'query': f"tag:{tag}",
        'limit': limit,
        'offset': offset,
        'fmt': 'json',
    }
    headers = {
        'User-Agent': USER_AGENT
    }
    try:
        r = requests.get(BASE_URL, params=params, headers=headers, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data
    except requests.HTTPError as e:
        print(f"Błąd HTTP: {e}")
        raise
    except requests.ConnectionError as e:
        print(f"Błąd z połączeniem: {e}")
        raise
    except requests.exceptions.Timeout as e:
        print(f"Przekroczono czas oczekiwania: {e}")
        raise
    except requests.exceptions.RequestException as e:
        print(f"Nieoczekiwany błąd: {e}")
        raise



def parse_artist(artist: dict) -> dict:
    life_span = artist.get('life-span', {})

    return {
        'mbid': artist['id'],
        'name': artist['name'],
        'type': artist.get('type'),
        'country': artist.get('country'),
        'begin': life_span.get('begin'),
        'end': life_span.get('end'),
        'ended': life_span.get('ended'),
    }

def print_artist(artist: dict, index: int) -> None:
    print(f"{index}. MBID: {artist['mbid']}, NAME: {artist['name']}, TYPE: {artist['type'] or 'brak'}, COUNTRY: {artist['country'] or 'brak'}, BEGIN: {artist['begin'] or 'brak'}, END: {artist['end'] or 'brak'}, ENDED: {artist['ended']}")


data = fetch_artist('rock', 25, 50)

for i, artist in enumerate(data['artists'], start=1):
    art = parse_artist(artist)
    print_artist(art, i)


