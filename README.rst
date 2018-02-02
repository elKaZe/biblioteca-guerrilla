====================
Biblioteca Guerrilla
====================



Simple static website generator to share books 🕮



### ¿ Que es ?
Biblioteca Guerrilla es una aplicacion para generar un catalogo web de libros
y embeberlo en un router ( o cualquier dispositivo :D).

### ¿ y como funciona esto ?
Actualmente la unica manera de genrar el catalogo es usando una biblioteca de [Calibre](https://calibre-ebook.com/),

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
generamos la web estatica *es importante que te muevas al directorio _app_*:
```
cd app/
python freeze.py
```
dentro de **app/build/** tedremos la web.

### ¿Como iniciar el server de pruebas?

Ejecutamos el siguiente comando
```
./start_test_server.sh
```

Ingresamos a http://localhost:5000/ para ver el sitio

### ¡ Quiero colabrar !
- Si encontras errores levantá un issue.
- ¡Los parches son más que bienvenidos!
- Si queres traducir entra
[acá](https://translate.zanata.org/project/view/biblioteca-guerrilla)

### ¿ Que licencia tiene ?
GPLv3+, chequea el archivo [LICENCE](LICENCE)

---------------------------


Credits
---------
Inspirado en [Letras viajeras](https://github.com/gcoop-libre/letras_viajeras/)
de la cooperativa [GCOOP](https://www.gcoop.coop/)

Tema basado en [aside](https://github.com/dansup/bulma-templates/blob/gh-pages/css/aside.css) de [dansup](https://github.com/dansup) con licencia MIT



This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

* Free software: GNU General Public License v3
