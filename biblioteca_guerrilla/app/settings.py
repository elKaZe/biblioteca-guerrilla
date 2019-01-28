# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.
#
#
import os

PROJECT_PATH = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]


# Admin data
ADMIN_NAME = "kaze"
ADMIN_EMAIL = "kaze@rlab.be"

# General settings
BASE_BOOK_PATH = os.path.realpath('~/books/')

# Connector
CONNECTOR = "connector.calibre.calibre"
CONNECTOR_OPTIONS = {
    "path": BASE_BOOK_PATH,
}

# Frozen-Flask
FREEZER_DESTINATION = "/home/kz/mnt/bibliotecaguerrilla/"
FREEZER_RELATIVE_URLS = False

# Languages
BABEL_DEFAULT_LOCALE = "en"
