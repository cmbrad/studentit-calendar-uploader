import logging


class Roster(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.shifts = []

    def __repr__(self):
        return '{!s}({!r})'.format(self.__class__, self.__dict__)

    def add_shift(self, shift):
        self.shifts.append(shift)
