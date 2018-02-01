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

# Connector
CONECTOR = "conector.calibre.calibre"
CONECTOR_OPCIONES = {
    "ruta": os.path.realpath(PROJECT_PATH+'/tests/data/\
biblioteca_calibre2/metadata.db'),
}
RUTA_BASE_LIBROS = os.path.realpath(PROJECT_PATH+'/tests/data/\
biblioteca_calibre2/')

# Frozen-Flask
FREEZER_DESTINATION = "/tmp/biblioteca-guerrilla/"
FREEZER_RELATIVE_URLS = False

# Languages
BABEL_DEFAULT_LOCALE = "en"
