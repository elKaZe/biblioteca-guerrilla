#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.

"""
Functions to make easy to work with books

"""

import os

from .urls import urlencode


def add_tags(books, connector):
    """add tags"""

    for book in books:
        tags = connector.get_tags_from_book(book.get("id", ''))
        book["tags"] = tags
    return books


def add_format(books, connector):
    """Add the file type and the path of the book using a dict
    ex: book["format"] -> {'pdf', '/tmp/book.pdf'}"""

    for book in books:
        dic_format = {}
        format = connector.get_formats(book['id'])
        for element_fomart in format:
            filet_type = (element_fomart[0]).lower()
            file_name = element_fomart[1] + "." + filet_type

            file_path = os.path.join(
                book['path'],
                file_name)
            # Encode at saving
            dic_format[filet_type] = urlencode(file_path)

        book["format"] = dic_format

    return books


def add_cover_path(books, connector):
    """Add the the path of the cover the the list of books, the "book" is a
    dictionary"""

    cover_file_name = "cover.jpg"

    for book in books:
        ruta_cover = os.path.join(
            book.get('path'),
            cover_file_name)
        book["cover"] = urlencode(ruta_cover)

    return books


def simplify_date(books):
    """simplify the date
    ej: 0101-01-01 00:00:00+00:00
        0101
        """

    for book in books:
        # Obtengo el año de publicacion, que son los primeros 4 caracteres
        book["publication_date"] = book.get("publication_date", "")[:4]

    return books


def add_authors(books, connector):
    """Add the authors of the book"""

    for book in books:
        authors = connector.get_author_of_book(book.get("id", ''))
        book["authors"] = authors

    return books


def add_synopsis(books, connector):
    """Add the synopsis of the book"""

    for book in books:
        synopsis = connector.get_synopsis(book.get("id", ''))
        book["sinopsis"] = "".join(synopsis)

    return books


def add_series(books, connector):
    """Add the series of the book"""

    for book in books:
        series = connector.get_series_from_book(book.get("id", ''))
        book["series"] = series
    return books


def normalize_book(books, connector):
    "Normalize the attributes of books"

    books = simplify_date(books)
    books = add_tags(books, connector)
    books = add_synopsis(books, connector)
    books = add_authors(books, connector)
    books = add_series(books, connector)
    books = add_format(books, connector)
    normalized_books = add_cover_path(books, connector)
    return normalized_books
