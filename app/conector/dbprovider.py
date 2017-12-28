# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.

"""Utilidades para la base de datos"""

import abc
from importlib import import_module

import settings


class ConectorABS(metaclass=abc.ABCMeta):
    """Metaclase para que extiendan los conectores"""
    @abc.abstractmethod
    def __init__():
        """Inicializar"""
        pass

    @abc.abstractmethod
    def conectar():
        """Conectar y crear cursor"""
        pass

    @abc.abstractmethod
    def desconectar():
        """Desconectar"""
        pass

    @abc.abstractmethod
    def obtener_todos():
        """Obtiene todos los libros"""
        pass

    @abc.abstractmethod
    def obtener_por_autor(self, autor):
        """Obtiene todos de un autor"""
        pass

    @abc.abstractmethod
    def obtener_autores_de_libro(self, id_libro):
        """Obtiene los autores de un libro"""

    @abc.abstractmethod
    def obtener_autores():
        """Obtiene todos los autores de la biblioteca"""
        pass

    @abc.abstractmethod
    def obtener_por_nombre(self, nombre_libro):
        """Obtiene un libro por su nombre"""
        pass

    @abc.abstractmethod
    def obtener_por_serie(self, serie):
        """Obtiene todos de una serie"""
        pass

    @abc.abstractmethod
    def obtener_por_etiqueta(self, etiqueta):
        """Obtiene todos de una etiqueta"""
        pass

    @abc.abstractmethod
    def obtener_etiquetas_de_libro(self, id_libro):
        """Obtiene las etiquetas de un libro"""
        pass

    @abc.abstractmethod
    def obtener_series_de_libro(self, id_libro):
        """Obtiene las series de un libro"""
        pass

    @abc.abstractmethod
    def obtener_etiquetas():
        """Obtiene todas las etiquetas"""
        pass

    @abc.abstractmethod
    def obtener_formatos(self, id_libro):
        """Obtiene todos los formatos de un libro
        devuelve un listado con el formato y el nombre del archivo"""
        pass

    @abc.abstractmethod
    def obtener_sinopsis(self, id_libro):
        """Obtiene la sinopsis de un libro"""
        pass


def instanciar_conector():
    """Inicializa e instancia el conector segun la configuracion"""

    # Importamos el modulo
    modulo = import_module(settings.CONECTOR)
    # Instanciamos al conector
    con = modulo.Conector(**settings.CONECTOR_OPCIONES)
    return con
