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


def agregar_etiquetas(libros, conector):
    """Agrega el formato en forma de diccionario con su ruta al archivo
    ej libro["formato"] -> -{'pdf': '/tmp/libro.pdf'}"""

    for libro in libros:
        libro['etiquetas'] = conector.obtener_etiquetas_de_libro(\
                libro.get('id'))
    return libros

def agregar_formatos(libros, conector):
    """Agrega el formato en forma de diccionario con su ruta al archivo
    ej libro["formato"] -> -{'pdf': '/tmp/libro.pdf'}"""

    for libro in libros:
        dic_formato = {}
        formatos = conector.obtener_formatos(libro['id'])
        for elem_formato in formatos:
            tipo_fichero = (elem_formato[0]).lower()
            nombre_archivo = elem_formato[1] + "." + tipo_fichero

            ruta_fichero = os.path.join(RUTA_BASE_LIBROS,
                    libro['ruta'],
                    nombre_archivo)
            dic_formato[tipo_fichero] = ruta_fichero

        libro["formatos"] = dic_formato

    return libros

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

    for libro in libros:
        etiquetas = conector.obtener_etiquetas_de_libro(libro.get("id", ''))
        libro["etiquetas"] = etiquetas
    return libros

def agregar_autores(libros, conector):
    """Añade los autores de un libro"""

    for libro in libros:
        autores = conector.obtener_autores_de_libro(libro.get("id", ''))
        libro["autores"] = autores

    return libros

def agregar_sinopsis(libros, conector):
    """Añade las etiquetas de un libro"""

    for libro in libros:
        sinopsis = conector.obtener_sinopsis(libro.get("id", ''))
        libro["sinopsis"] = "".join(sinopsis)

    return libros

def agregar_series(libros, conector):
    """Añade las etiquetas de un libro"""

    for libro in libros:
        series = conector.obtener_series_de_libro(libro.get("id", ''))
        libro["series"] = series
    return libros

def normalizar_libros(libros, conector):
    """Se encarga de normalizar los atributos de los libros"""

    libros = simplificar_fecha(libros)
    libros = agregar_etiquetas(libros, conector)
    libros = agregar_sinopsis(libros, conector)
    libros = agregar_autores(libros, conector)
    libros = agregar_series(libros, conector)
    libros = agregar_formatos(libros, conector)
    libros_normalizado = agregar_ruta_cover(libros, conector)
    return libros_normalizado
