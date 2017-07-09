# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the GPLv3+ license.

import sys
import os
import sqlite3
import logging
from app.dbprovider import ConectorABS


class Conector(ConectorABS):
    """conector a la base de datos de calibre, da unos metodos para conseguir
    info de la db"""

    def __init__(self, **kwargs):
        # Ruta a la db de calibre
        self.db = kwargs.get('ruta', '')
        # Logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        if not os.path.isfile(self.db):
            self.logger.critical("No se encuentra la base de datos de Calibre")
            raise FileNotFoundError("Base de datos de calibre no encontrada")

    def conectar(self):
        # conectamos y creamos el cursor
        self.con = sqlite3.connect(self.db)
        self.cursor = self.con.cursor()

    def desconectar(self):
        try:
            self.con.disconnect()
        except:
            pass

    def obtener_todos(self):
        # Obtenemos los metadatos de cada libro
        self.cursor.execute("""
        select id, title,  pubdate, path
        from books
        order by title;
        """)
        # retornamos la lista de autores
        ret = []
        for registro in self.cursor.fetchall():
            ret.append({"id": registro[0],
                        "titulo": registro[1],
                        "fecha_publicacion": registro[2],
                        "ruta": registro[3],
                        })
        return ret

    def obtener_por_nombre(self, nombre):
        self.cursor.execute("""
        select b.id, b.title, b.pubdate, b.path
        from books b
        where b.title = ?
        order by b.title""", (nombre,))

        ret = []
        for registro in self.cursor.fetchall():
            ret.append({"id": registro[0],
                        "titulo": registro[1],
                        "fecha_publicacion": registro[2],
                        "ruta": registro[3],
                        })
        return ret

    def obtener_por_autor(self, autor):
        # Obtenemos los metadatos de cada libro
        self.cursor.execute("""
        select b.id, b.title, b.pubdate, b.path
        from books b,  authors a
        where b.author_sort = a.sort and a.name = ?
        order by b.title""", (autor,))

        ret = []
        for registro in self.cursor.fetchall():
            ret.append({"id": registro[0],
                        "titulo": registro[1],
                        "fecha_publicacion": registro[2],
                        "ruta": registro[3],
                        })
        return ret

    def obtener_autores_de_libro(self, id_libro):
        self.cursor.execute("""
        select a.name
        from authors a,  books_authors_link bal
        where bal.id = a.id and bal.book = ?""", (id_libro,))

        ret = []
        for registro in self.cursor.fetchall():
            ret.append(registro[0])
        return ret

    def obtener_etiquetas_de_libro(self, id_libro):
        # Obtenemos los metadatos de cada libro

        self.cursor.execute("""
        select t.name
        from tags t,  books_tags_link btl
        where btl.tag = t.id and btl.book = ?
        order by t.name""", (id_libro,))

        ret = []
        for registro in self.cursor.fetchall():
            ret.append(registro[0])
        return ret

    def obtener_series_de_libro(self, id_libro):
        # Obtenemos los metadatos de cada libro

        self.cursor.execute("""
        select s.name
        from series s,  books_series_link bsl
        where bsl.series = s.id and bsl.book = ?
        order by s.name""", (id_libro,))

        ret = []
        for registro in self.cursor.fetchall():
            ret.append(registro[0])
        return ret

    def obtener_sinopsis(self, id_libro):
        # Obtenemos los metadatos de cada libro

        self.cursor.execute("""
        select c.text
        from comments c
        where c.book = ? """, (id_libro,))

        ret = []
        for registro in self.cursor.fetchall():
            ret.append(registro[0])
        return ret

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

    def obtener_por_etiqueta(self, etiqueta):
        self.cursor.execute("""
        select distinct b.id, b.title, b.pubdate, b.path
        from books b, tags t, books_tags_link btl
        where btl.book = b.id and btl.tag = t.id and t.name = ?
        order by b.title""", (etiqueta,))

        # retornamos la lista de libros
        ret = []
        for registro in self.cursor.fetchall():
            ret.append({"id": registro[0],
                        "titulo": registro[1],
                        "fecha_publicacion": registro[2],
                        "ruta": registro[3],
                        })
        print(ret)
        return ret

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

    def obtener_formatos(self, id_libro):
        """devuelve el listado de extensiones de los libros en un set"""

        # formato, nombre fichero
        self.cursor.execute("""
                            select format, name
                            from data
                            where book=?""", (id_libro,))

        # retornamos la lista de formatos
        ret = []
        for registro in self.cursor.fetchall():
            ret.append(registro)
        return ret
