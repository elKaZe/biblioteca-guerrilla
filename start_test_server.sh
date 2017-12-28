#! /usr/bin/bash

#Activo el virtualenv
#las variables de entorno
#corro el servidor de pruebas

if [ -z "$VIRTUAL_ENV" ]; then
    source venv/bin/activate && echo "Venv OK" || echo "Venv FAIL"
fi


export FLASK_DEBUG=1
export FLASK_APP=main.py
pushd app
python -m flask run
popd
