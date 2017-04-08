import logging


class RosterUploader(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def upload(self, roster):
        raise NotImplementedError

