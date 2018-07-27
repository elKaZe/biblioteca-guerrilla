# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.

"""Utilities for the database"""

import abc
from importlib import import_module

import settings


class ConnectorABS(metaclass=abc.ABCMeta):
    """Metaclass to make connectors extend it"""
    @abc.abstractmethod
    def __init__():
        """Initialize"""
        pass

    @abc.abstractmethod
    def connect():
        """Connect and create db cursor"""
        pass

    @abc.abstractmethod
    def desconnect():
        """Desconnect"""
        pass

    @abc.abstractmethod
    def get_all():
        """Get all the books"""
        pass

    @abc.abstractmethod
    def get_by_author(self, author):
        """Obtain all books from an author"""
        pass

    @abc.abstractmethod
    def get_author_of_book(self, book_id):
        """Obtain the authors of a book"""

    @abc.abstractmethod
    def get_authors():
        "Obtain all the authors in the library"
        pass

    @abc.abstractmethod
    def get_book_by_name(self, book_name):
        "Obtain a book by its name"
        pass

    @abc.abstractmethod
    def get_books_by_serie(self, serie):
        "Obtains all the books from a serie"
        pass

    @abc.abstractmethod
    def get_books_by_tag(self, tag):
        "Obtain all the books with the tag"""
        pass

    @abc.abstractmethod
    def get_tags_from_book(self, book_id):
        "Get tags from a book"
        pass

    @abc.abstractmethod
    def get_series_from_book(self, book_id):
        "Obtain the tags from a book"
        pass

    @abc.abstractmethod
    def get_tags():
        "Obtain all the tags"
        pass

    @abc.abstractmethod
    def get_formats(self, book_id):
        "Returns a list with the all the formats and the name of the file"
        pass

    @abc.abstractmethod
    def get_synopsis(self, book_id):
        "Get the synopsis of a book"
        pass


def instance_connector():
    "Initialize and instance the connector according the configuration"

    # Import the module
    module = import_module(settings.CONNECTOR)
    # Instance the module
    con = module.Connector(**settings.CONNECTOR_OPTIONS)
    return con
