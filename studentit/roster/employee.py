import logging
import sqlite3


class Employee(object):
    def __init__(self, name, email_address=None):
        self.name = name
        self.email_address = email_address or self._email_address_from_name()

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

    def _email_address_from_name(self):
        conn = sqlite3.connect('people.db')
        c = conn.cursor()
        # Add a % to wildcard the search to account for surnames in the database
        c.execute('SELECT email FROM Employees where name LIKE ?', [self.name + '%'])
        email_addresses = c.fetchall()
        # Is returned as a list of one element tuples, flatten it
        email_addresses = [address[0] for address in email_addresses]

        if not email_addresses:
            raise Exception(f'No email address for {self.name} in the database')
        if len(email_addresses) > 1:
            raise Exception(f'{self.name} could map to multiple email addresses. Make the name more specific or '
                            f'update the database. Emails: {", ".join(email_addresses)}')

        return email_addresses[0][0]
