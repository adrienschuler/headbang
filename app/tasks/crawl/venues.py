import os
import requests

from bs4 import BeautifulSoup

from luigi.contrib.esindex import CopyToIndex

from app import logger
from app.core.models import Concert


class UrbanSpree(CopyToIndex):
    host = os.getenv('ES_HOST', 'localhost')
    port = 9200
    index = 'headbang'
    doc_type = 'venue'
    purge_existing_index = True

    def docs(self):
        url = 'https://www.urbanspree.com/program/concerts/'
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        print(soup.prettify())

        raise
