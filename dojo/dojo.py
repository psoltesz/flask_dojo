import os
from peewee import *
from dojo.connectdatabase import ConnectDatabase
from dojo.models import flask_dojo
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app


app = Flask(__name__)
app.secret_key = 'super secret key'  # the app needs a secret key for POST functions as I discovered


def init_db():
    ConnectDatabase.db.connect()
    ConnectDatabase.db.create_tables([flask_dojo], safe=True)


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'postgre_db'):
        g.postgre_db.close()
