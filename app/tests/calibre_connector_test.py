#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Distributed under terms of the GPLv3+ license.

import os
import unittest

from dbprovider import ConectorABS
from conector.calibre import Conector

"""
Test para  el conector de calibre

"""


class CalibreConnectorTestCase(unittest.TestCase):

    def setUp(self):
        self.con = Conector(
            "tests/data/biblioteca_calibre/metadata.db")
        self.con.conectar()

    def tearDown(self):
        self.con.desconectar()

    def test_instancia(self):
        """verifica que extienda y sea instancia de dbprovider"""
        self.assertTrue(
            issubclass(Conector, ConectorABS)
        )
        self.assertTrue(
            isinstance(
                Conector(
                    "tests/data/biblioteca_calibre/metadata.db"),
                ConectorABS))

        # Verificamos el error al pasarle una ruta invalida
        with self.assertRaises(FileNotFoundError):
            Conector("")

    def test_obtener_autores(self):
        """Testeamos la obtencion de autores"""
        # tenemos tres
        autores = self.con.obtener_autores()
        self.assertEqual(len(autores), 3)

    def test_obtener_todos(self):
        """Testeamos la obtencion todo"""
        # tenemos tres
        libros = self.con.obtener_todos()
        self.assertEqual(len(libros), 3)

        # cantidad de atributos
        for l in libros:
            self.assertEqual(len(l), 4)

    def test_obtener_etiquetas(self):
        """Testeamos la obtencion de etiquetas"""
        etiquetas = self.con.obtener_etiquetas()
        self.assertEqual(len(etiquetas), 5)

    def test_obtener_por_etiquetas(self):
        """Traemos todos los libros por cada etiqueta"""

        etiquetas = self.con.obtener_etiquetas()
        for e in etiquetas:
            libros = self.con.obtener_por_etiqueta(e)
            self.assertNotEqual(len(libros), 0)

        # Etiqueta inexistente
        libros = self.con.obtener_por_etiqueta("asddwjijijij")
        self.assertEqual(len(libros), 0)

    def test_obtener_formatos(self):
        """Traemos los formatos de un libro"""

        libros = self.con.obtener_todos()

        for l in libros:
            formatos = self.con.obtener_formatos(l[0])
            self.assertNotEqual(len(formatos), 0)

        # Sin formatos
        formatos = self.con.obtener_formatos("8798798798798")
        self.assertEqual(len(formatos), 0)


if __name__ == '__main__':
        unittest.main()
