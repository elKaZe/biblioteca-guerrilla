.PHONY: clean clean-test clean-pyc clean-build docs help start-test-server generate-static-website
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

# lint: ## check style with flake8
# 	flake8 biblioteca_guerrilla tests

# test: ## run tests quickly with the default Python

# 		python setup.py test

# test-all: ## run tests on every Python version with tox
# 	tox

# coverage: ## check code coverage quickly with the default Python
# 	coverage run --source biblioteca_guerrilla setup.py test
# 	coverage report -m
# 	coverage html
# 	$(BROWSER) htmlcov/index.html

# docs: ## generate Sphinx HTML documentation, including API docs
# 	rm -f docs/biblioteca_guerrilla.rst
# 	rm -f docs/modules.rst
# 	sphinx-apidoc -o docs/ biblioteca_guerrilla
# 	$(MAKE) -C docs clean
# 	$(MAKE) -C docs html
# 	$(BROWSER) docs/_build/html/index.html

# servedocs: docs ## compile the docs watching for changes
# 	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

# release: clean ## package and upload a release
# 	python setup.py sdist upload
# 	python setup.py bdist_wheel upload

# dist: clean ## builds source and wheel package
# 	python setup.py sdist
# 	python setup.py bdist_wheel
# 	ls -l dist

# install: clean ## install the package to the active Python's site-packages
# 	python setup.py install

start-test-server: clean ## runs tests server to see what the app generates
	export FLASK_DEBUG=1; export FLASK_APP=main.py; cd biblioteca_guerrilla/app; python -m flask run

generate-static-website: clean ## generate the static website
	cd biblioteca_guerrilla/app; python freeze.py

babel-extract-messages: ## extracts strings from code to translate
	pybabel  extract --project='Biblioteca Guerrilla' --sort-by-file  -F babel.cfg  -o  messages/messages.pot biblioteca_guerrilla/app/

babel-compile-translations: ## compile translations
	pybabel compile -f -d biblioteca_guerrilla/app/translations

