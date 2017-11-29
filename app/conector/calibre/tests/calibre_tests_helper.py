#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import faker
import tempfile
import subprocess

class CalibreTestsHelper(object):

    """Get rid of books and relations"""

    def __init__(self, library_directory="/tmp/"):
        """

        :library_directory: directroy that will contain the library directory

        """
        self._library_directory= library_directory
        self.library_path = tempfile.mkdtemp(dir=self._library_directory)

        # calibredb and specifies the library path
        self.base_command = ["calibredb", "--library-path",self.library_path]

    def _run_command(self, command):
        """Run specified command

        :command: iterable object
        :returns: subprocess.run object

        """
        return subprocess.run(command, shell=True, check=True)


    def create_empty_library(self):
        """Create an empty library
        """
        command =  self.base_command

        _run_command(command)



    def destroy(self):
        """Will delete temporal library
        """
        self.library_path.close()

