# -*- coding: utf-8 -*-
import click
import main
from flask_frozen import Freezer

freezer = Freezer(main.app)


def freeze_with_progressbar():
    """Freeze the site with a nice progress bar"""
    with click.progressbar(
            freezer.freeze_yield(),
            item_show_func=lambda p: p.url if p else 'Done!') as urls:
        for url in urls:
            # everything is already happening, just pass
            pass
