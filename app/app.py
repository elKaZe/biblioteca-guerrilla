# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.

"""

"""

from app.dbprovider import instanciar_conector
from app.utils_libro import normalizar_libros
from flask import Flask, render_template, send_from_directory, url_for
app = Flask('__name__')
# Levantamos la config
app.config.from_object("app.settings")

# Filtros


def obtener_filtros():
    """Filtros para la barra izquierda"""
    filtros = (
        {'url': url_for('vista_autores'),
         'nombre': "Autores"},
        # {'url': url_for('categorias'),
        # 'nombre': "Categorias"},
        # {'url': url_for('idiomas'),
        # 'nombre': "Idiomas"},
        # {'url': url_for('series'),
        # 'nombre': "Series"},
    )
    return filtros


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

 # Miscelaneo


def obtener_autores_con_url():
    """Devuelve una lista con todos los autores"""
    autores = []

    conector = instanciar_conector()
    conector.conectar()
    # obtenemos los autores sin procesar
    autores_crudo = conector.obtener_autores()
    for autor in autores_crudo:
        url = url_for('vista_autor_especificado', nombre_autor=autor)
        autores.append({'url': url, 'elemento': autor})

    conector.desconectar()
    return autores

# Vistas


@app.route('/')
def index():
	return render_template('index.html',
                        titulo="¡Biblioteca Guerrilla!",
                        filtros_generales=obtener_filtros()
                        )


@app.route('/autor/<string:nombre_autor>/')
def vista_autor_especificado(nombre_autor):
    """Muestra los libros de un autor"""
    libros = filtrar_por_autor(nombre_autor)

    return render_template("listado_de_libros.html",
                           libros=libros,
                           titulo=nombre_autor,
                           filtros_generales=obtener_filtros()
                           )


@app.route('/etiqueta/<string:nombre_etiqueta>/')
def vista_etiqueta_especificada(nombre_etiqueta):
    """Muestra los libros de una etiquea"""
    libros = filtrar_por_etiqueta(nombre_etiqueta)

    return render_template("listado_de_libros.html",
                           libros=libros,
                           titulo=nombre_etiqueta,
                           filtros_generales=obtener_filtros()
                           )


@app.route('/libro/<string:nombre_libro>/')
def vista_libro_especificado(nombre_libro):
    """Muestra el libro pedido"""
    libros = filtrar_por_nombre(nombre_libro)

    return render_template("libro.html",
                           libro=libros[0],
                           titulo=nombre_libro,
                           filtros_generales=obtener_filtros()
                           )


@app.route('/autores/')
def vista_autores():
    """Lista los autores """
    autores = obtener_autores_con_url()

    return render_template("listado_de_entradas.html",
                           entradas=autores,
                           titulo="Autores",
                           filtros_generales=obtener_filtros(),
                           path='autor'
                           )


@app.route('/tapas/<path:ruta>')
def devolver_tapa(ruta):
    return send_from_directory('', ruta)
