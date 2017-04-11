import logging


class Location(object):
    def __init__(self, name):
        self.name = name

        self.logger = logging.getLogger(__name__)

    def __repr__(self):
        return '{!s}({!r})'.format(self.__class__, self.__dict__)
