# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the GPLv3+ license.

import sys, os, time, string, re
import sqlite3
import logging
from dbprovider import Conector

class Calibre_connector(Conector):
    """conector a la base de datos de calibre, da unos metodos para conseguir
    info de la db"""

    def __init__(self, ruta):
        self.db = ruta
        if not os.path.isfile(self.db):
            logger.critical("No se encuentra la base de datos de Calibre")
            sys.exit(0)

        # conectamos y creamos el cursor
        self.con = sqlite3.connect(self.db)
        self.cursor = self.con.cursor()


    def obtener_todos(self):
        # Obtenemos los metadatos de cada libro
        self.cursor.execute("""
        select uuid, title, author_sort, pubdate
        from books
        order by title;
        """)
        # retornamos la lista de autores
        ret = []
        for registro in self.cursor.fetchall():
            ret.append(registro)
        return ret

    def obtener_por_autor(self, autor):
        # Obtenemos los metadatos de cada libro
        self.cursor.execute("""
        select b.uuid, b.title, b.author_sort, b.pubdate
        from books b,  authors a
        where b.author_sort = a.sort and a.name = ?
        order by b.title""", autor)

    def obtener_autores(self):
        self.cursor.execute("""
        select name
        from authors
        order by name""")
        # retornamos la lista de autores
        ret = []
        for registro in self.cursor.fetchall():
            ret.append(registro[0])
        return ret


    def obtener_por_serie(self, serie):
        pass

    def obtener_por_etiqueta(self, serie):
        self.cursor.execute("""
        select b.uuid, b.title, b.author_sort, b.pubdate
        from books b, tags t, books_tags_link btl
        where btl.tag = b.id and t.name = ?
        order by b.title""", serie)

    def obtener_etiquetas(self):
        self.cursor.execute("""
        select name
        from tags
        order by name""")

        # retornamos la lista de etiqueta
        ret = []
        for registro in self.cursor.fetchall():
            ret.append(registro[0])
        return ret

    def obtener_formatos(id_libro):
        """devuelve el listado de extensiones de los libros en un set"""





