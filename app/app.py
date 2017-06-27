# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
# Distributed under terms of the GPLv3+ license.

"""

"""


from flask import Flask, render_template
app = Flask('__name__')
# Levantamos la config
app.config.from_object("settings")


@app.route('/')
@app.route('/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)


@app.route('/u/')
def show_user_profile():
        # show the user profile for that user
        return render_template('aside.html')
