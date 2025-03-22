import requests
import time
from typing import Optional, List, Dict, Any
from functools import reduce

def generate_x_enigma():
    def f(e: str) -> list[int]:
        return [ord(char) for char in e]
    
    bait_string = "<img src='/getbaited.jpg' />"
    bait_bytes = f(bait_string)
    
    def w3(e: str) -> list[int]:
        return [ord(char) for char in e]
    
    def n5(e: list[int]) -> int:
        return bait_bytes[0] if not e else reduce(lambda acc, curr: acc ^ curr, bait_bytes, e[0])
    
    def _t(e: int) -> str:
        return ('0' + hex(e)[2:])[-2:]
    
    timestamp = str(420 * int(time.time() * 1000) + 69)
    return ''.join(_t(n5(w3(char))) for char in timestamp)

async def get_song_stats_listeners(
    artist_name: str,
    city: str,
    country: Optional[str] = None
) -> Optional[str]:
    headers = {
        "accept": "application/json",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "fe-build-timestamp": str(int(time.time() * 1000)),
        "fe-platform": "web",
        "fe-version": "143",
        "origin": "https://songstats.com/",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://songstats.com/",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "x-enigma": generate_x_enigma()
    }

    try:
        # Search for artist
        search_url = f"https://data.songstats.com/api/v1/search/search_all?q={requests.utils.quote(artist_name)}&excludedModels=RadioStation"
        search_response = requests.get(search_url, headers=headers)
        search_data = search_response.json()
        artist_id = search_data["results"][0]["idUnique"]

        # Get map stats
        params = {
            "idUnique": artist_id,
            "source": "spotify"
        }
        response = requests.get(
            "https://data.songstats.com/api/v1/audience/map_stats",
            params=params,
            headers=headers
        )
        resp = response.json()

        # Get the number of listeners for city
        country_code = country or "GB"
        for row in resp["mapStats"][0]["data"]["rows"]:
            if row["countryCode"] == country_code:
                for city_row in row["rowGroup"]:
                    if city_row["cityName"] == city:
                        return city_row["cells"][1]["displayText"]
        
        return None

    except Exception as error:
        print(f"Error fetching SongStats listeners: {error}")
        return None

if __name__ == "__main__":
    import asyncio
    
    async def main():
        listeners = await get_song_stats_listeners("The Weeknd", "London")
        print(f"The Weeknd has {listeners} listeners in London")
    
    asyncio.run(main()) 