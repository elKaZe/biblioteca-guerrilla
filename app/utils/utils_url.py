#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Facundo Acevedo <facevedo[AT]openmailbox[DOT]org>
#
# Distributed under terms of the GPLv3+ license.

"""
Funciones para laburar con urls
"""

import urllib


def urlencode(s):
    s = urllib.parse.quote_plus(s)
    return s


def urldecode(s):
    s = urllib.parse.unquote_plus(s)
    return s


