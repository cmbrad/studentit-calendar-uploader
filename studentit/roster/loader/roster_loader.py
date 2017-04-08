import logging


class RosterLoader(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def load(self, path):
        raise NotImplementedError

