import logging

import click

from studentit.roster.roster import Roster
from .loader import XlsxLoader
from .uploader import GcalUploader
from ..config import Config


@click.group()
@click.pass_context
def cli(ctx):
    configure_logging()
    ctx.obj['LOGGER'] = logging.getLogger('studentit.roster.cli')


@cli.command(name='parse', help='Parsers a roster into a format the uploader can understand')
@click.option('--excel-filename', '-x', required=True)
@click.option('--config-filename', '-c', default='config.json')
@click.pass_obj
def parse(obj, excel_filename, config_filename):
    obj['LOGGER'].info('Starting with roster {} and config {}'.format(excel_filename, config_filename))

    config = Config().from_file(config_filename)
    roster = XlsxLoader(config['xlsx_loader']).load(excel_filename)
    roster.save()

    obj['LOGGER'].info('Complete')


@cli.command(name='upload', help='Uploads a roster from the given source to the given target')
@click.option('--roster-filename', '-r', required=True)
@click.option('--config-filename', '-c', default='config.json')
@click.pass_obj
def upload(obj, roster_filename, config_filename):
    obj['LOGGER'].info('Starting with roster {} and config {}'.format(roster_filename, config_filename))

    config = Config().from_file(config_filename)

    roster = Roster.load(roster_filename)
    GcalUploader(config['gcal_uploader']).upload(roster)

    obj['LOGGER'].info('Complete')


def configure_logging():
    # create logger
    logger = logging.getLogger('studentit')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)


if __name__ == '__main__':
    cli(obj={})
