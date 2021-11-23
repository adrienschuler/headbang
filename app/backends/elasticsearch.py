import os

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError

from app import logger


class ElasticsearchBackend:
    def __init__(self):
        self.host = {
            'host': os.getenv('ES_HOST', 'localhost'),
            'port': 9200,
            'use_ssl': False}
        self.connect()

    def connect(self):
        try:
            logger.debug(self.host)
            self.client = Elasticsearch([self.host])
            # logger.debug(self.client.info())
        except AttributeError:
            raise

    def search(self, query: str = None) -> list:
        try:
            response = []
            query = {'match': {'name': {'query': query}}}
            search = self.client.search(
                index='headbang',
                query=query)

            for doc in search['hits']['hits']:
                response.append(doc['_source'])

            return response
        except ConnectionError:
            logger.error(ConnectionError)
            self.connect()
            raise


ES = ElasticsearchBackend()
