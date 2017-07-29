import logging

from studentit.roster.uploader.exceptions import ShiftUploadError


class RosterUploader(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def upload(self, roster):
        success = failed = 0
        self.logger.info('Beginning roster upload')
        for shift in roster.shifts:
            try:
                self.logger.debug('Uploading shift {}'.format(shift))
                self._upload_shift(shift)
                success += 1
            except ShiftUploadError as e:
                failed += 1
                self.logger.error(repr(e))
        self.logger.info(f'Roster upload complete with {success} success and {failed} failures')

    def _upload_shift(self, shift):
        raise NotImplementedError
