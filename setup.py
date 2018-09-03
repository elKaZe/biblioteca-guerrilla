#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pip.req import parse_requirements
"""The setup script."""

from setuptools import setup
install_requires = parse_requirements('requirements.txt', session='hack')

setup()
