# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the GPLv3+ license.

import logging
import os
import sqlite3
from flask_babel import gettext as _

from connector.dbprovider import ConnectorABS


class Connector(ConnectorABS):
    """Connect to the calibre database and provides an API to it"""

    def __init__(self, **kwargs):
        # path to db
        self.db = kwargs.get('path', '')
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        if not os.path.isfile(self.db):
            self.logger.critical(_("Database not found."))
            raise FileNotFoundError(_("Database not found."))

    def connect(self):
        # connect and create the cursor
        self.con = sqlite3.connect(self.db)
        self.cursor = self.con.cursor()

    def desconnect(self):
        try:
            self.con.disconnect()
        except BaseException:
            pass

    def get_all(self):
        # Get the metadata of each book
        self.cursor.execute("""
        select id, title,  pubdate, path
        from books
        order by title;
        """)
        # reaturn a listf of authors
        ret = []
        for register in self.cursor.fetchall():
            ret.append({"id": register[0],
                        "title": register[1],
                        "publication_date": register[2],
                        "path": register[3],
                        })
        return ret

    def get_book_by_name(self, name):
        self.cursor.execute("""
        select distinct b.id, b.title, b.pubdate, b.path
        from books b
        where b.title = ?
        order by b.title""", (name,))

        ret = []
        for register in self.cursor.fetchall():
            ret.append({"id": register[0],
                        "title": register[1],
                        "publication_date": register[2],
                        "path": register[3],
                        })
        return ret

    def get_by_author(self, author):
        # Get the metadata of each book by author
        self.cursor.execute("""
        select distinct b.id, b.title, b.pubdate, b.path
        from books b,  authors a
        where b.author_sort like "%"||a.sort||"%" and a.name like  ?
        order by b.title""", ("%" + author + "%",))

        ret = []

        for register in self.cursor.fetchall():
            ret.append({"id": register[0],
                        "title": register[1],
                        "publication_date": register[2],
                        "path": register[3],
                        })

        return ret

    def get_author_of_book(self, book_id):
        self.cursor.execute("""
        select distinct a.name
        from authors a,  books_authors_link bal
        where bal.author= a.id and bal.book = ?""", (book_id,))

        ret = []
        for register in self.cursor.fetchall():
            ret.append(register[0])
        return ret

    def get_tags_from_book(self, book_id):

        self.cursor.execute("""
        select t.name
        from tags t,  books_tags_link btl
        where btl.tag = t.id and btl.book = ?
        order by t.name""", (book_id,))

        ret = []
        for register in self.cursor.fetchall():
            ret.append(register[0])
        return ret

    def get_synopsis(self, book_id):

        self.cursor.execute("""
        select c.text
        from comments c
        where c.book = ? """, (book_id,))

        ret = []
        for register in self.cursor.fetchall():
            ret.append(register[0])
        return ret

    def get_authors(self):
        self.cursor.execute("""
        select name
        from authors
        order by name""")
        # retornamos la lista de authors
        ret = []
        for register in self.cursor.fetchall():
            ret.append(register[0])
        return ret

    def get_books_by_serie(self, serie):
        self.cursor.execute("""
        select distinct b.id, b.title, b.pubdate, b.path
        from books b, series s, books_series_link bsl
        where bsl.book = b.id and bsl.series = s.id and s.name = ?
        order by b.title""", (serie,))

        # return the list of books
        ret = []
        for register in self.cursor.fetchall():
            ret.append({"id": register[0],
                        "title": register[1],
                        "publication_date": register[2],
                        "path": register[3],
                        })
        return ret

    def obtener_series(self):
        self.cursor.execute("""
        select s.name
        from series s
        order by s.name""")
        ret = []
        for register in self.cursor.fetchall():
            ret.append(register[0])
        return ret

    def get_series_from_book(self, book_id):
        self.cursor.execute("""
        select s.name
        from series s,  books_series_link bsl
        where bsl.series = s.id and bsl.book = ?
        order by s.name""", (book_id,))

        ret = []
        for register in self.cursor.fetchall():
            ret.append(register[0])
        return ret

    def get_books_by_tag(self, tag):
        self.cursor.execute("""
        select distinct b.id, b.title, b.pubdate, b.path
        from books b, tags t, books_tags_link btl
        where btl.book = b.id and btl.tag = t.id and t.name = ?
        order by b.title""", (tag,))

        ret = []
        for register in self.cursor.fetchall():
            ret.append({"id": register[0],
                        "title": register[1],
                        "publication_date": register[2],
                        "path": register[3],
                        })
        return ret

    def get_tags(self):
        self.cursor.execute("""
        select name
        from tags
        order by name""")

        ret = []
        for register in self.cursor.fetchall():
            ret.append(register[0])
        return ret

    def get_formats(self, book_id):
        """Return a list of file extension of the books in a set"""

        # format, file name
        self.cursor.execute("""
                            select format, name
                            from data
                            where book=?""", (book_id,))

        ret = []
        for register in self.cursor.fetchall():
            ret.append(register)
        return ret
