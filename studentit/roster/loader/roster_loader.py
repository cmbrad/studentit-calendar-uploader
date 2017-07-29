import logging


class RosterLoader(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__dict__})'

    def load(self, path):
        raise NotImplementedError
