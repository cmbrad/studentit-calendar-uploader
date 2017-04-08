import logging

import click


@click.group()
def cli():
    pass


@cli.command(name='validate', help='Checks if a given roster file is a valid file format')
@click.option('--filename', '-f', required=True)
def validate(filename):
    pass

