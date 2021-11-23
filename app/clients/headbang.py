import os
import requests

from app import logger


class HeadbangClient:
    def __init__(self):
        self.endpoint = "http://localhost:8000"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def callback(self) -> dict:
        response = requests.post(f'{self.endpoint}/callback',
            headers=self.headers,).json()
        logger.debug(response)
        return response


Headbang = HeadbangClient()
