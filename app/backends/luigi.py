import os

from app import logger


class LuigiBackend:
    def __init__(self):
        pass

    def trigger(self):
        command = "PYTHONPATH='.' python -m luigi --module app.tasks.spotify FollowedArtists"
        response = os.system(command)
        logger.debug(response)
        return response


Luigi = LuigiBackend()
