# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.

"""

"""
from connector.dbprovider import instance_connector
from flask import (Flask, redirect, render_template, send_from_directory,
                   url_for)
from flask_babel import gettext as _
from flask_babel import Babel
from settings import BASE_BOOK_PATH
from utils.books import normalize_book
from utils.urls import urldecode, urlencode

app = Flask('__name__')

# Set up
app.config.from_object("settings")
babel = Babel(app)


# Filters

def get_filters():
    """Filters on the left bar"""
    filters = (
        {'url': url_for('all_the_books_view'),
         'name': _("Books"),
         'iconclass': "fa fa-book"},
        {'url': url_for('authors_view'),
         'name': _("Authors"),
         'iconclass': "fa fa-users"},
        {'url': url_for('tags_view'),
         'name': _("Categories"),
         'iconclass': "fa fa-list"},
        # {'url': url_for('idiomas'),
        # 'name': _("Langueges"),
        # 'fa-icon-class': "fa fa-language"},
        {'url': url_for('series_view'),
         'name': _("Series"),
         'iconclass': "fa fa-indent"},
    )
    return filters


def get_admin_data():
    """Get Admin data form config file
    :returns: dicct

    """
    admin_data = {
        'name': app.config.get("ADMIN_NAME", _("Not set")),
        'email': app.config.get("ADMIN_EMAIL", _("Not set")),
    }
    return admin_data


def get_stats():
    """
    Gets stats about the amount of books, series, tags and authors
    :returns: dicct

    """

    stats = {'authors': len(filter_by_author()),
             'categories': len(get_tags_with_url()),
             'books': len(get_books()),
             'series': len(get_collections_with_url()),
             }

    return stats


def filter_by_author(author=""):
    connector = instance_connector()
    connector.connect()
    # get books without processing
    books = connector.get_by_author(author)
    # Lets normalize the list f books
    books = normalize_book(books, connector)
    connector.desconnect()
    return books


def filter_by_tag(tag=""):
    connector = instance_connector()
    connector.connect()
    # get books without processing
    books = connector.get_books_by_tag(tag)
    # Lets normalize the list f books
    books = normalize_book(books, connector)
    connector.desconnect()
    return books


def filter_by_collection(serie=""):
    connector = instance_connector()
    connector.connect()
    serie = urldecode(serie)
    # get books without processing
    books = connector.get_books_by_serie(serie)
    # Lets normalize the list f books
    books = normalize_book(books, connector)
    connector.desconnect()
    return books


def filter_by_book_name(book_name=""):
    """Filter by the name of the book"""
    connector = instance_connector()
    connector.connect()
    # get books without processing
    books = connector.get_book_by_name(book_name)
    # Lets normalize the list f books
    books = normalize_book(books, connector)
    connector.desconnect()
    return books


def get_books():
    """Get all books and normalize them
    :returns: list

    """
    connector = instance_connector()
    connector.connect()
    # get books without processing
    books = connector.get_all()
    # Lets normalize the list f books
    books = normalize_book(books, connector)
    connector.desconnect()
    return books


def get_collections_with_url():
    """Get a list with all the series"""
    series = []

    connector = instance_connector()
    connector.connect()
    # Get seriers without processing
    raw_series = connector.obtener_series()
    for serie in raw_series:
        serie_safe = urlencode(serie)
        url = url_for('collection_view', serie_name=serie_safe)
        series.append({'url': url, 'element': serie})

    connector.desconnect()
    return series


def get_tags_with_url():
    """Get a list with all the tags"""
    tags = []

    connector = instance_connector()
    connector.connect()
    # Get tags without processing
    tags_raw = connector.get_tags()
    for tag in tags_raw:
        tag_safe = urlencode(tag)
        url = url_for(
            'tag_view',
            tag_name=tag_safe)
        tags.append({'url': url, 'element': tag})

    connector.desconnect()
    return tags


def get_authors_with_url():
    """Get a list with all the authors"""
    authors = []

    connector = instance_connector()
    connector.connect()
    # Get authors without processing
    authors_raw = connector.get_authors()
    for author in authors_raw:
        autor_safe = urlencode(author)
        url = url_for(
            'author_view',
            author_name=autor_safe)
        authors.append({'url': url, 'element': author})

    connector.desconnect()
    return authors


def format_elements_for_template(elements):
    """Generate a dict with the first key of the element as key and the element as value"""

    first_letter_dict = {}
    for element in elements:
        # Inside element there is two items, 'url' and 'element'
        first_letter = element.get('element')[0].upper()
        if first_letter_dict.get(first_letter, None) is None:
            first_letter_dict[first_letter] = []

        first_letter_dict[first_letter].append(element)
    return first_letter_dict

# Views


@app.route('/')
def index():
    return render_template('index.html',
                           title="",
                           general_filters=get_filters(),
                           stats=get_stats(),
                           admin=get_admin_data(),
                           )


@app.route('/books/')
def all_the_books_view():
    """Show the books"""
    books = get_books()

    return render_template("list_of_books.html",
                           books=books,
                           title=_("All books:"),
                           general_filters=get_filters()
                           )


@app.route('/author/<path:author_name>/')
def author_view(author_name):
    """Muestra los books de un author"""
    if not author_name:
        return redirect(url_for('authors_view'))

    author_name = urldecode(author_name)
    books = filter_by_author(author_name)

    return render_template("list_of_books.html",
                           books=books,
                           title=author_name,
                           general_filters=get_filters()
                           )


@app.route('/author/')
def redirect_author():
    return redirect(url_for('authors_view'))


@app.route('/serie/<path:serie_name>/')
def collection_view(serie_name):
    """Shows books with a particular tag"""
    if not serie_name:
        return redirect(url_for('series_view'))

    serie_name = urldecode(serie_name)
    books = filter_by_collection(serie_name)

    return render_template("list_of_books.html",
                           books=books,
                           title=serie_name,
                           general_filters=get_filters()
                           )


@app.route('/serie/')
def redirect_serie():
    return redirect(url_for('series_view'))


@app.route('/tag/<path:tag_name>/')
def tag_view(tag_name):
    """Shows books with a particular tag"""
    if not tag_name:
        return redirect(url_for('tags_view'))

    tag_name = urldecode(tag_name)
    books = filter_by_tag(tag_name)

    return render_template("list_of_books.html",
                           books=books,
                           title=tag_name,
                           general_filters=get_filters(),
                           )


@app.route('/tag/')
def redirect_tag():
    return redirect(url_for('tags_view'))


@app.route('/book/<path:book_name>/')
def book_view(book_name):
    """Shows a particular book"""
    book_name = urldecode(book_name)
    books = filter_by_book_name(book_name)

    return render_template("book.html",
                           book=books[0],
                           title=book_name,
                           general_filters=get_filters()
                           )


@app.route('/book/')
def redirect_book():
    return redirect(url_for('index'))


@app.route('/authors/')
def authors_view():
    """List of authors """
    authors = get_authors_with_url()
    authors = format_elements_for_template(authors)

    return render_template("list_of_entries.html",
                           entries=authors,
                           title=_("Authors"),
                           general_filters=get_filters(),
                           path='author'
                           )


@app.route('/tags/')
def tags_view():
    """List of tags"""
    tags = get_tags_with_url()
    tags = format_elements_for_template(tags)

    return render_template("list_of_entries.html",
                           entries=tags,
                           title=_("Categories"),
                           general_filters=get_filters(),
                           path='tags'
                           )


@app.route('/series/')
def series_view():
    """List of series"""
    series = get_collections_with_url()
    series = format_elements_for_template(series)

    return render_template("list_of_entries.html",
                           entries=series,
                           title=_("Series"),
                           general_filters=get_filters(),
                           path='series'
                           )


@app.route('/covers/<path:path>')
def get_book_cover(path):
    safe_path = urldecode(path)
    return send_from_directory(BASE_BOOK_PATH, safe_path)


@app.route('/file/<path:path>')
def get_book_download(path):
    safe_path = urldecode(path)
    return send_from_directory(BASE_BOOK_PATH, safe_path, as_attachment=True)


# Allow to use this function from templates
@app.context_processor
def utility_processor():
    return dict(urlencode=urlencode)
