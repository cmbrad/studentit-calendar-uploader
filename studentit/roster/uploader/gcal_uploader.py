from studentit.roster.uploader.exceptions import ShiftUploadError
from .roster_uploader import RosterUploader


class GcalUploader(RosterUploader):
    def __init__(self, calendars, environment='test'):
        super().__init__()

        self.environment = environment
        self.calendars = calendars

    def _upload_shift(self, shift):
        calendar = self.calendars.get(shift.location.lower(), {}).get(self.environment)
        if calendar is None:
            raise NoCalendarError(shift.location.lower(), self.environment, shift)

        self.logger.debug(f'Uploading {shift} to {calendar}')
        self._make_event(calendar, shift)

    def _make_event(self, calendar_id, shift):
        raise NotImplementedError


class NoCalendarError(ShiftUploadError):
    def __init__(self, location, environment, shift):
        self.location = location
        self.environment = environment
        self.shift = shift
