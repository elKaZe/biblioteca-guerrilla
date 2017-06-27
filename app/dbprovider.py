# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.

"""ABC para proveer de varias db a la aplicacion"""

import abc

class Conector(metaclass=abc.ABCMeta):
    """Metaclase para que extiendan los conectores"""

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
