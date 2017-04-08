from .roster_uploader import RosterUploader


class GcalUploader(RosterUploader):
    def __init__(self, calendars):
        super().__init__()

        self.calendars = calendars

    def _upload_shift(self, shift):
        self.logger.debug('Uploading shift {}'.format(shift))

