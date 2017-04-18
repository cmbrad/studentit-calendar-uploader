import logging


class RosterUploader(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def upload(self, roster):
        self.logger.info('Beginning roster upload')
        for shift in roster.shifts:
            self.logger.debug('Uploading shift {}'.format(shift))
            self._upload_shift(shift)
        self.logger.info('Roster upload complete')

    def _upload_shift(self, shift):
        raise NotImplementedError

