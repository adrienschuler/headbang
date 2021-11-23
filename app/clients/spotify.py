import os
import requests

from app import logger


class SpotifyClient:
    def __init__(self):
        self.endpoint = "https://api.spotify.com/v1"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('SPOTIFY_OAUTH_TOKEN')}",
        }

    def get_artist(self, artist_id: str = None) -> dict:
        response = requests.get(f'{self.endpoint}/artists/{artist_id}',
            headers=self.headers,).json()
        logger.debug(response)
        return response

    def get_followed_artists(self, next_request: str = None) -> dict:
        request = f'{self.endpoint}/me/following?type=artist&limit=50'
        if next_request:
            request = next_request
        response = requests.get(request,
            headers=self.headers,).json()
        logger.debug(response)
        return response


Spotify = SpotifyClient()
