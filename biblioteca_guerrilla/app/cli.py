from flask_babel import gettext as _
from freeze import freeze_with_progressbar
import main

import click


@click.command()
@click.option('--ip-address', '-a', default="127.0.0.1", help=_('Sets the ip address. Default: 127.0.0.1'))
@click.option('--port', '-p', default=8080, help=_('Sets the port. Default: 8080.'))
def live(ip_address, port):
    """Runs a live server"""
    main.app.run(host=ip_address, port=port)


@click.command()
@click.option('--destination', '-d', help=_('Destination path where the static site will be generated.'))
def generate_static_site(destination):
    """Generates the static site"""
    freeze_with_progressbar()


if __name__ == '__main__':
    live()
