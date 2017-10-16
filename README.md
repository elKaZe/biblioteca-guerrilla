Biblioteca Guerrilla
========

### ¿ Que es ?
Biblioteca Guerilla es una aplicacion bastante basica para generar una
biblioteca online y embeberla en un router ( u otros dispositivos :D )

### ¿ y como funciona esto ?
A partir de una base de datos de [Calibre](https://calibre-ebook.com/), se
obtienen los metadatos, portadas y los libros en si, con esto generamos paginas
estaticas.


### Mandale mecha!
Asegurate que todos los libros tengan la portada generada, eso lo conseguis
desde calibre, chequea las opciones de **modificar metadatos en masa**

Edita __app/settings.py__:
```
CONECTOR_OPCIONES = {
    "ruta": "ruta/a/la/base/de/datos/de/calibre/metadata.db"
    }
RUTA_BASE_LIBROS = "ruta/a/la/bibliotecaDeCalibre/"
```
generamos la web estatica:
```
cd app/
python freeze.py
```

dentro de **app/build/** tedremos la web.


### ¿ Que licencia tiene ?
GPLv3+, chequea el archivo [LICENCE](LICENCE)

---------------------------

Inspirado en [Letras viajeras](https://github.com/gcoop-libre/letras_viajeras/)
de la cooperativa [GCOOP](https://www.gcoop.coop/)
Tema basado en [aside](https://github.com/dansup/bulma-templates/blob/gh-pages/css/aside.css) de [dansup](https://github.com/dansup) con licencia MIT