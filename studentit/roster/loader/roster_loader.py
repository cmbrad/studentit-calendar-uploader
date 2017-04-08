import logging


class RosterLoader(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def __repr__(self):
        return '{!s}({!r})'.format(self.__class__, self.__dict__)

    def load(self, path):
        raise NotImplementedError

