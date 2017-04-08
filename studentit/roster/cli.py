import logging

import click

from .loader import FileLoader


@click.group()
def cli():
    pass


@cli.command(name='upload', help='Uploads a roster from the given source to the given target')
@click.option('--filename', '-f', required=True)
def upload(filename):
    file_loader = FileLoader()
    roster = file_loader.load(filename)

    print(roster)
    print(file_loader)


@cli.command(name='validate', help='Checks if a given roster file is a valid file format')
@click.option('--filename', '-f', required=True)
def validate(filename):
    pass


if __name__ == '__main__':
    cli()

