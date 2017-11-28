#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import factory

class CalibreTestsHelper(object):

    """Get rid of books and relations"""

    def __init__(self, library_path="/tmp/"):
        """

        :library_path: path to create the library

        """
        self._library_path = library_path
