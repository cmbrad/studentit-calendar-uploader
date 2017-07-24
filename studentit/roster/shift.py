import logging


class Shift(object):
    def __init__(self, name, location, start_time, end_time):
        self.name = name
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

        self.logger = logging.getLogger(__name__)

    def __repr__(self):
        return '{!s}({!r})'.format(self.__class__, self.__dict__)
