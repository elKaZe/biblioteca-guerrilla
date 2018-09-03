# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.
#
#
import os

PROJECT_PATH = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]

# Flask DEBUG
DEBUG = True
# Admin data
ADMIN_NAME = "kaze"
ADMIN_EMAIL = "kaze@rlab.be"

# Connector
CONNECTOR = "connector.calibre.calibre"
CONNECTOR_OPTIONS = {
    "path": os.path.realpath('/home/facu/Biblioteca de calibre/metadata.db'),
}
BASE_BOOK_PATH = os.path.realpath('/home/facu/Biblioteca de calibre/')

# Frozen-Flask
FREEZER_DESTINATION = "/tmp/biblioteca-guerrilla/"
FREEZER_RELATIVE_URLS = False

# Languages
BABEL_DEFAULT_LOCALE = "es"
