Biblioteca Guerrilla
========

### ¿ Que es ?
Biblioteca Guerrilla es una aplicacion para generar un catalogo web de libros
y embeberlo en un router ( o cualquier dispositivo :D).

### ¿ y como funciona esto ?
Actualmente la unica manera de genrar el catalogo es usando una biblioteca de [Calibre](https://calibre-ebook.com/),

### Instalar

Vas a necesitar `pipenv` para correr todo.  Se puede instalar con

```
pip install pipenv
```

Y luego para instalar todas las dependencias:

```
pipenv install
```

Antes de generar el sitio, hay que entrar al entorno de trabajo:

```
pipenv shell
```

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
make generate-static-website
```
dentro de **/tmp/biblioteca-guerrilla/** tedremos la web.

### ¿Como iniciar el server de pruebas?

Ejecutamos el siguiente comando
```
make start-test-server
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

Inspirado en [Letras viajeras](https://github.com/gcoop-libre/letras_viajeras/)
de la cooperativa [GCOOP](https://www.gcoop.coop/)

Tema basado en [aside](https://github.com/dansup/bulma-templates/blob/gh-pages/css/aside.css) de [dansup](https://github.com/dansup) con licencia MIT
