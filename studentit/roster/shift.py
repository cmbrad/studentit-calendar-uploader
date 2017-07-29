import logging


class Shift(object):
    def __init__(self, employee, location, start_time, end_time):
        self.employee = employee
        self.location = location
        self.start_time = start_time
        self.end_time = end_time

        self.logger = logging.getLogger(__name__)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__dict__})'

    def __getstate__(self):
        d = self.__dict__.copy()
        if 'logger' in d.keys():
            d['logger'] = d['logger'].name
        return d

    def __setstate__(self, state):
        if 'logger' in state.keys():
            state['logger'] = logging.getLogger(state['logger'])
        self.__dict__.update(state)
