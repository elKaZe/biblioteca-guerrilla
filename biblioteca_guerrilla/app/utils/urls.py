#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Kaze <kaze[AT]rlab[DOT]be>
#
# Distributed under terms of the GPLv3+ license.

"""
Functions to work with urls
"""

import urllib


def urlencode(s, safe="/"):
    s = urllib.parse.quote_plus(s, safe=safe)
    return s


def urldecode(s):
    s = urllib.parse.unquote_plus(s)
    return s
