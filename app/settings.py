# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.

######### Connector
CONECTOR = "conector.calibre.calibre"
CONECTOR_OPCIONES = {
    "ruta": "tests/data/biblioteca_calibre2/metadata.db",
}
RUTA_BASE_LIBROS = "tests/data/biblioteca_calibre2"

######### Frozen-Flask
FREEZER_DESTINATION = "/tmp/biblioteca-guerrilla/"

######### Languages
SUPPORTED_LANGUAGES = {'es': 'Español', 'en': 'English'}
BABEL_DEFAULT_LOCALE = "es"
