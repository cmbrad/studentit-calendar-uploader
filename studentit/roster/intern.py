import logging


class Intern(object):
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address

        self.logger = logging.getLogger(__name__)

    def __repr__(self):
        return '{!s}({!r})'.format(self.__class__, self.__dict__)

