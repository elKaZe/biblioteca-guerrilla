# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.

"""Utilidades para la base de datos"""

from importlib import import_module
import abc
import app.settings as settings


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
    def obtener_por_autor(autor):
        """Obtiene todos de un autor"""
        pass

    @abc.abstractmethod
    def obtener_autores():
        """Obtiene todos los autores"""
        pass

    @abc.abstractmethod
    def obtener_por_serie(serie):
        """Obtiene todos de una serie"""
        pass

    @abc.abstractmethod
    def obtener_por_etiqueta(etiqueta):
        """Obtiene todos de una etiqueta"""
        pass

    @abc.abstractmethod
    def obtener_etiquetas():
        """Obtiene todas las etiquetas"""
        pass

    @abc.abstractmethod
    def obtener_formatos(id_libro):
        """Obtiene todos los formatos de un libro"""
        pass


def instanciar_conector():
    """Inicializa e instancia el conector segun la configuracion"""

    # Importamos el modulo
    modulo = import_module(settings.CONECTOR)
    # Instanciamos al conector
    con = modulo.Conector(**settings.CONECTOR_OPCIONES)
    return con
