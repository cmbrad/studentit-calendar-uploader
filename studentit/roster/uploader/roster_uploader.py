import logging


class RosterUploader(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def upload(self, roster):
        for shift in roster.shifts:
            self._upload_shift(shift)

    def _upload_shift(self, shift):
        raise NotImplementedError

