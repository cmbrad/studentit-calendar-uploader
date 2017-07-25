import logging

import click

from .loader import XlsxLoader
from .uploader import GcalUploader
from ..config import Config


@click.group()
@click.pass_context
def cli(ctx):
    configure_logging()
    ctx.obj['LOGGER'] = logging.getLogger('studentit.roster.cli')


@cli.command(name='upload', help='Uploads a roster from the given source to the given target')
@click.option('--roster-filename', '-r', required=True)
@click.option('--config-filename', '-c', required=True)
@click.pass_obj
def upload(obj, roster_filename, config_filename):
    obj['LOGGER'].info('Starting with roster {} and config {}'.format(roster_filename, config_filename))

    config = Config().from_file(config_filename)

    loader = XlsxLoader(config['xlsx_loader'])
    uploader = GcalUploader(config['gcal_uploader'])

    roster = loader.load(roster_filename)
    uploader.upload(roster)

    obj['LOGGER'].info('Complete')


@cli.command(name='validate', help='Checks if a given roster file is a valid file format')
@click.option('--filename', '-f', required=True)
def validate(filename):
    pass


def configure_logging():
    # create logger
    logger = logging.getLogger('studentit')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)


if __name__ == '__main__':
    cli(obj={})
