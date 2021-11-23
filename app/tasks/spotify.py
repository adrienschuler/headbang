import os
import time

import luigi
from luigi.contrib.esindex import CopyToIndex

from app import logger
from app.clients.spotify import Spotify
from app.clients.headbang import Headbang
from app.core.models import Artist


class FollowedArtists(CopyToIndex):
    host = os.getenv('ES_HOST', 'localhost')
    port = 9200
    index = 'headbang'
    doc_type = 'artist'
    purge_existing_index = True

    def docs(self):
        next_request = None
        while True:
            response = Spotify.get_followed_artists(next_request)
            for artist in response['artists']['items']:
                doc = Artist(**artist).json()
                logger.debug(doc)
                yield doc

            if 'next' in response['artists'] and response['artists']['next'] is not None:
                next_request = response['artists']['next']
                time.sleep(0.5)
            else:
                break

    @luigi.Task.event_handler(luigi.Event.SUCCESS)
    def callback(task):
        """Will be called directly after a successful execution
           of `run` on any Task subclass (i.e. all luigi Tasks)
        """
        Headbang.callback()
