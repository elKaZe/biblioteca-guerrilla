#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the GPLv3+ license.

"""
Test para  el connector de calibre

"""

import unittest

from app.connector.calibre import Connector
from app.dbprovider import ConnectorABS


class CalibreConnectorTestCase(unittest.TestCase):

    def setUp(self):
        self.con = Connector(
            **{'path': "app/tests/data/biblioteca_calibre/metadata.db"})
        self.con.connect()

    def tearDown(self):
        self.con.desconnect()

    def test_instancia(self):
        """verifica que extienda y sea instancia de dbprovider"""
        self.assertTrue(
            issubclass(Connector, ConnectorABS)
        )
        self.assertTrue(
            isinstance(
                Connector(
                    **
                    {'path': "app/tests/data/biblioteca_calibre/metadata.db"}),
                ConnectorABS))

        # Verificamos el error al pasarle una path invalida
        with self.assertRaises(FileNotFoundError):
            Connector(**{'path': ""})

    def test_get_authors(self):
        """Testeamos la obtencion de authors"""
        # tenemos tres
        authors = self.con.get_authors()
        self.assertEqual(len(authors), 3)

    def test_get_all(self):
        """Testeamos la obtencion todo"""
        # tenemos tres
        books = self.con.get_all()
        self.assertEqual(len(books), 3)

        # cantidad de atributos
        for l in books:
            self.assertEqual(len(l), 4)

    def test_get_by_author(self):
        """Traemos todos los books por cada author"""

        authors = self.con.get_authors()
        for a in authors:
            books = self.con.get_by_author(a)
            self.assertNotEqual(len(books), 0)

    def test_get_tags(self):
        """Testeamos la obtencion de tags"""
        tags = self.con.get_tags()
        self.assertEqual(len(tags), 5)

    def test_get_books_by_tags(self):
        """Traemos todos los books por cada tag"""

        tags = self.con.get_tags()
        for e in tags:
            books = self.con.get_books_by_tag(e)
            self.assertNotEqual(len(books), 0)

        # Etiqueta inexistente
        books = self.con.get_books_by_tag("asddwjijijij")
        self.assertEqual(len(books), 0)

    def test_get_formats(self):
        """Traemos los format de un book"""

        books = self.con.get_all()

        for l in books:
            format = self.con.get_formats(l.get("id"))
            self.assertNotEqual(len(format), 0)

        # Sin format
        format = self.con.get_formats("8798798798798")
        self.assertEqual(len(format), 0)


if __name__ == '__main__':
    unittest.main()
