import logging
import pickle


class Roster(object):
    logger = logging.getLogger(__name__)

    def __init__(self, start_date, end_date):
        self.shifts = []
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return '{!s}({!r})'.format(self.__class__, self.__dict__)

    def __getstate__(self):
        d = self.__dict__.copy()
        if 'logger' in d.keys():
            d['logger'] = d['logger'].name
        return d

    def __setstate__(self, state):
        if 'logger' in state.keys():
            state['logger'] = logging.getLogger(state['logger'])
        self.__dict__.update(state)

    def add_shift(self, shift):
        self.shifts.append(shift)

    def save(self, path=None):
        if path is None:
            path = f'{self.start_date.strftime("%y_%m_%d")}-{self.end_date.strftime("%y_%m_%d")}.roster'
        self.logger.info(f'Saving roster with {len(self.shifts)} shifts')
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, path):
        with open(path, 'rb') as f:
            roster = pickle.load(f)
            cls.logger.info(f'Loaded roster with {len(roster.shifts)} shifts')
        return roster
