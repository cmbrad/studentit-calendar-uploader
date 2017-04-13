import os
import re
import errno
from pathlib import Path

import dateutil.parser
from openpyxl import load_workbook

from ..roster import Roster
from .roster_loader import RosterLoader


# Colour index of a blank cell in the worksheet
BLANK_COLOUR = '00000000'


class XlsxLoader(RosterLoader):
    def __init__(self, config):
        super().__init__()

        self.config = config

    def load(self, path):
        self.logger.debug('Loading roster from file at {}'.format(path))
        if not Path(path).is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

        sheet = self._sheet(path)
        start_date, end_date = self._date_range(sheet)
        roster = Roster(start_date=start_date, end_date=end_date)

        print(sheet['C2'].fill.start_color.index)
        print(sheet['C3'].fill.start_color.index)
        print(sheet['C4'].fill.start_color.index)
        print(sheet['C5'].fill.start_color.index)
        print(sheet['C6'].fill.start_color.index)
        print(sheet['C7'].fill.start_color.index)
        print(sheet['C8'].fill.start_color.index)
        print(sheet['F7'].fill.start_color.index)
        print(sheet['F10'].fill.start_color.index)

        return roster

    def _sheet(self, path):
        self.logger.debug('Loading workbook')
        wb = load_workbook(path)

        # Always just use the first worksheet
        sheet = wb.worksheets[0]
        self.logger.debug('Using sheet {}'.format(sheet.title))

        return sheet

    def _date_range(self, sheet):
        date_cell_ref = self.config['date_cell']
        cell_format = self.config['date_cell_format']

        date_cell_text = sheet[date_cell_ref].value

        if date_cell_text is None:
            raise Exception('No text in date cell ({}). Check if cell reference is correct in the config file.'.format(date_cell_ref))

        matches = re.findall(cell_format, date_cell_text)
        if len(matches) != 1:
            raise Exception('Invalid text format in date cell ({}). Text: {}'.format(date_cell_ref, date_cell_text))

        dates = matches[0]
        if len(dates) != 2:
            raise Exception('Invalid text format in date cell ({}). Text: {}'.format(date_cell_ref, date_cell_text))

        start_date = dateutil.parser.parse(dates[0])
        end_date = dateutil.parser.parse(dates[1])
        end_date = end_date.replace(hour=23, minute=59, second=59)

        self.logger.info('Roster spanning {} - {}'.format(start_date, end_date))

        return start_date, end_date
