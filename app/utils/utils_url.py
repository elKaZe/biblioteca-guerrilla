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


def urlencode(s, safe="/"):
    s = urllib.parse.quote_plus(s, safe=safe)
    return s


def urldecode(s):
    s = urllib.parse.unquote_plus(s)
    return s
