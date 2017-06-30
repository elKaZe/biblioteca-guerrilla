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


@app.route('/tapas/<path:ruta>')
def devolver_tapa(ruta):
    return send_from_directory('', ruta)
