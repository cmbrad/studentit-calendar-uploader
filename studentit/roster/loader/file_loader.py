import os
import errno
from pathlib import Path


from ..roster import Roster
from .roster_loader import RosterLoader


class FileLoader(RosterLoader):
    def __init__(self):
        super().__init__()

    def load(self, path):
        self.logger.debug('Loading roster from file at {}'.format(path))
        if not Path(path).is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

        return Roster()

