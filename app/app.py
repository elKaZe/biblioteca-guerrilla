# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.

"""

"""

from app.dbprovider import instanciar_conector
from app.utils_libro import normalizar_libros
from flask import Flask, render_template, send_from_directory
app = Flask('__name__')
# Levantamos la config
app.config.from_object("app.settings")

# Filtros


def obtener_filtros():
    """Filtros para la barra izquierda"""
    filtros = {
        "todos": (
            (url_for('autores'), "Autores"),
            (url_for('categirias'), "Categorias"),
            (url_for('series'), "Series"),
            (url_for('idiomas'), "Idiomas"),
        )
    }


def filtrar_por_autor(autor):
    conector = instanciar_conector()
    conector.conectar()
    # obtenemos los libros sin procesar
    libros = conector.obtener_por_autor(autor)
    #Normalizamos la lista de libros
    libros = normalizar_libros(libros, conector)
    conector.desconectar()
    return libros

def filtrar_por_etiqueta(etiqueta):
    conector = instanciar_conector()
    conector.conectar()
    # obtenemos los libros sin procesar
    libros = conector.obtener_por_etiqueta(etiqueta)
    #Normalizamos la lista de libros
    libros = normalizar_libros(libros, conector)
    conector.desconectar()
    return libros


def filtrar_por_nombre(nombre_libro):
    """Filtra por el nombre del libro"""
    conector = instanciar_conector()
    conector.conectar()
    # obtenemos los libros sin procesar
    libros = conector.obtener_por_nombre(nombre_libro)
    #Normalizamos la lista de libros
    libros = normalizar_libros(libros, conector)
    conector.desconectar()
    return libros

def separar_en_columnas(libros):
    """Devuelvo una lista con n listas de libros.
    para poder mostrarlos ecolumnados pero en orden alfabetico
    en el html"""
    lista1 = []
    lista2 = []
    lista3 = []

    for i, libro in enumerate(libros):
        if i%3 == 0:
            lista3.append(libro)
        elif i%2 == 0:
            lista2.append(libro)
        else:
            lista1.append(libro)
    return [lista1, lista2, lista3]


@app.route('/')
def index():
	return render_template('hello.html', name=name)


@app.route('/autor/<string:nombre_autor>/')
def vista_autor_especificado(nombre_autor):
    """Muestra los libros de un autor"""
    libros = filtrar_por_autor(nombre_autor)

    return render_template("listado.html",
                           libros=libros,
                           titulo=nombre_autor,
                           )

@app.route('/etiqueta/<string:nombre_etiqueta>/')
def vista_etiqueta_especificada(nombre_etiqueta):
    """Muestra los libros de una etiquea"""
    libros = filtrar_por_etiqueta(nombre_etiqueta)
    libros = separar_en_columnas(libros)

    return render_template("listado.html",
                           libros=libros,
                           titulo=nombre_etiqueta,
                           )


@app.route('/libro/<string:nombre_libro>/')
def vista_libro_especificado(nombre_libro):
    """Muestra el libro pedido"""
    libros = filtrar_por_nombre(nombre_libro)

    return render_template("libro.html",
                           libro=libros[0],
                           titulo=nombre_libro,
                           )


@app.route('/tapas/<path:ruta>')
def devolver_tapa(ruta):
    return send_from_directory('', ruta)
