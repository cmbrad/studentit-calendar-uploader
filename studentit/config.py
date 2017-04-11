import json
import logging


class Config(object):
    def __init__(self):
        self._data = {}
        self.logger = logging.getLogger(__name__)

    def from_file(self, filename):
        self.logger.debug('Loading config from {}'.format(filename))
        with open(filename, 'r') as f:
            self._data = json.load(f)

        return self 

    def __getitem__(self, key):
        return self._data[key]

    def get(self, key, default=None):
        return self._data.get(key, default)
