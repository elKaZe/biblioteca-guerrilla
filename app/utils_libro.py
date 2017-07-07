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

    nombre_fichero_tapa = "cover.jpg"

    for libro in libros:
        ruta_cover = os.path.join(RUTA_BASE_LIBROS,
                                  libro.get('ruta'),
                                  nombre_fichero_tapa)
        libro["tapa"] = ruta_cover

    return libros


def simplificar_fecha(libros):
    """Simplifica la fecha
    ej: 0101-01-01 00:00:00+00:00
        0101
        """

    for libro in libros:
        # Obtengo el año de publicacion, que son los primeros 4 caracteres
        libro["fecha_publicacion"] = libro.get("fecha_publicacion", "")[:4]

    return libros


def agregar_etiquetas(libros, conector):
    """Añade las etiquetas de un libro"""

    nuevo_libros = []
    nombre_fichero_tapa = "cover.jpg"

    for libro in libros:

        libro["etiquetas"] = \
            conector.obtener_etiquetas_de_libro(libro.get("titulo"), '')

    return libros


def normalizar_libros(libros, conector):
    """Se encarga de normalizar los atributos de los libros"""

    libros = simplificar_fecha(libros)
    libros_normalizado = agregar_ruta_cover(libros, conector)
    return libros_normalizado
