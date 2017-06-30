#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.

import os
from app.settings import RUTA_BASE_LIBROS

"""
Funciones que laburan con los libros

"""


def agregar_ruta_cover(libros, conector):
    """Agrega la ruta de la tapa del libro a la lista de libros, el libro es un
    diccionario"""

    nuevo_libros = []
    nombre_fichero_tapa = "cover.jpg"

    for libro in libros:
        ruta_cover = os.path.join(RUTA_BASE_LIBROS,
                                  libro.get('ruta'),
                                  nombre_fichero_tapa)
        libro["tapa"] = ruta_cover

        nuevo_libros.append(libro)

    return nuevo_libros


def normalizar_libros(libros, conector):
    """Se encarga de normalizar los atributos de los libros"""

    libros_normalizado = agregar_ruta_cover(libros, conector)
    return libros_normalizado
