import os
import errno
from pathlib import Path

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

        self.logger.debug('Loading workbook')
        wb = load_workbook(path)
        self.logger.debug('Loading roster from {} worksheets: {}'.format(
            len(wb.worksheets), ', '.join(wb.get_sheet_names())
        ))
        for sheet in wb.worksheets:
            self.logger.debug('Loading from sheet {}'.format(sheet.title))

            print(sheet['C2'].fill.start_color.index)
            print(sheet['C3'].fill.start_color.index)
            print(sheet['C4'].fill.start_color.index)
            print(sheet['C5'].fill.start_color.index)
            print(sheet['C6'].fill.start_color.index)
            print(sheet['C7'].fill.start_color.index)
            print(sheet['C8'].fill.start_color.index)
            print(sheet['F7'].fill.start_color.index)
            print(sheet['F10'].fill.start_color.index)

        return Roster()
