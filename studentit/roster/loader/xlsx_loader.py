import os
import re
import errno
from pathlib import Path

import dateutil.parser
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, coordinate_from_string, column_index_from_string

from ..roster import Roster
from .roster_loader import RosterLoader


class XlsxLoader(RosterLoader):
    def __init__(self, config):
        super().__init__()

        self.config = config

    def load(self, path):
        self.logger.debug('Loading roster from file at {}'.format(path))
        if not Path(path).is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

        ws = self._sheet(path)
        start_date, end_date = self._date_range(ws)
        roster = Roster(start_date=start_date, end_date=end_date)

        people = self._people(ws)

        people_col_num, people_start_row = self._split_coords(self.config['people_start_cell'])
        for i in range(0, len(people)):
            people_col = get_column_letter(people_col_num)
            name = ws['{}{}'.format(people_col, people_start_row)].value

            self.logger.debug('Parsing shifts for {}'.format(name))

            for people_row in range(people_start_row + 1, 10):
                cell = ws['{}{}'.format(people_col, people_row)]
                print(cell.value, cell.fill.start_color.index)
            people_col_num += 1

        return roster

    def _split_coords(self, cell_ref):
        col, row = coordinate_from_string(self.config['people_start_cell'])
        return column_index_from_string(col), row

    def _people(self, ws):
        people = []
        for row in ws.iter_rows('C6:ZZ6'):
            for cell in row:
                if cell.value is None:
                    break
                people.append(cell.value)
        return people

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
            raise Exception('No text in date cell ({}). Check if cell reference is correct in the config file.'.format(
                date_cell_ref))

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
