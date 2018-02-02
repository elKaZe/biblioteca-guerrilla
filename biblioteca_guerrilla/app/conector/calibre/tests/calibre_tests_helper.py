# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# -*- coding: utf-8 -*-


#import subprocess
#import tempfile

#import epubaker
#import faker

# Library components to consider:
# colections -> (name)
# books ->(name, author, published, sinopsis, tags, formats, publishing
# house)


# def create_epub(**data):
#    """Create the ebook
#    :returns: Book object

#    """
#    book = epubaker.Epub3
#    book.metadata.append(epubaker.Title=data.get("title"))
#    book.metadata.append(
#        epubaker)
#    book = mkepub.Book(
#        title=data.get("title"),
#        authors=data.get("authors"))

#    book.save(data.get(path))
#    return book


# class CalibreTestsHelper(object):

#    """Get rid of books and relations"""

#    def __init__(self, library_directory="/tmp/"):
#        """

#        :library_directory: directroy that will contain the library directory

#        """
#        self._library_directory = library_directory
#        self.library_path = tempfile.mkdtemp(dir=self._library_directory)

#        # calibredb and specifies the library path
#        self.base_command = ["calibredb", "--library-path", self.library_path]

#        self.faker = Faker()

#    def _run_command(self, command):
#        """Run specified command

#        :command: iterable object
#        :returns: subprocess.run object

#        """
#        return subprocess.run(command, shell=True, check=True)

#    def create_empty_library(self):
#        """Create an empty library
#        """
#        command = self.base_command

#        _run_command(command)

#    def create_collection(self, ammount):
#        """Create a collection by the same authors

#        :ammount: integer - length of the collection
#        :returns: TODO

#        """
#        collection = []
#        author = self.faker.name()
#        collection = self.faker.safe_color_name()

#        for b in ammount:
#            title = self.faker.job()
#            book = create_epub({"title": title,
#                                "author": author,
#                                "collection": collection_name})
#            collection_of_books.append()

#    def destroy(self):
#        """Will delete temporal library
#        """
#        self.library_path.close()
