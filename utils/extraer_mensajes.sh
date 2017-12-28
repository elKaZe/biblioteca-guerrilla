#! /bin/env bash

# Extrae las lineas a traducir

pybabel  extract --project='Biblioteca Guerrilla' --sort-by-file  -F babel.cfg  -o  messages/messages.pot app/
