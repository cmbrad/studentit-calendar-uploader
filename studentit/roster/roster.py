import logging


class Roster(object):
    def __init__(self, start_date, end_date):
        self.logger = logging.getLogger(__name__)
        self.shifts = []
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return '{!s}({!r})'.format(self.__class__, self.__dict__)

    def add_shift(self, shift):
        self.shifts.append(shift)
