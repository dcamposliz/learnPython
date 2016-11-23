# Flaskr Tutorial: A Microblogging App

Source: [Flaskr Tutorial](http://flask.pocoo.org/docs/0.11/tutorial/introduction/)

In this tutorial we create a simple micro-blogging application. It only supports one user that can create text-only entries. We will use Flask and SQLite as a database (which comes out of the box with Python).

This tutorial requires `Python 2`.

Specifications:

 - Let the user sign in and out with credentials specified in the configuration. Only one user is supported.

 - When the user is logged in, they can add new entries to the page consisting of a text-only title and some HTML for the text. This HTML is not sanitized because we trust the user here.

 - The index page shows all entries so far in reverse chronological order (newest on top) and the user can add new ones from there if logged in.

 The steps necessary to create this application are the following:

  - Creating the Directories

  - Database Schema

  - Application Setup Code

  - Database Connections

  - Creating the Database

  - The View Functions

  - The Templates

  - Adding Style

  - Testing the Application

# Step 0: Creating the directories

We need this directory structure for the application:

    /flaskr
      /static
      /templates

The files inside `/static` are available to the users of the application via HTTP. This is where the CSS and JavaScript files go.

Inside the `templates` folder, Flaskr will look for the `Jinga2` templates. The templates you create later in this tutorial will go in this directory.

# Step 1: Database Schema

Create a file named `schema.sql` in the flaskr directory. Enter the following code:

    drop table if exists entries;
    create table entries (
      id integer primary key autoincrement,
      title text not null,
      'text' text not null
    );

This schema consists of a single table called `entries`.

Each row in this table has an `id`, a `title`, and a `text`.

The id is an automatically incrementing integer and a primary key, the other two are strings that must not be null.

# Step 2: Application Setup Code

Create `flaskr.py` in the `flaskr` directory.

Proceed to add the imports:


    # all the imports
    import os
    import sqlite3
    from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash


Next, we create our actual application and initialize it with the config from the same file in `flaskr.py`:


    # create our little application :)
    app = Flask(__name__)
    app.config.from_object(__name__)

    # load default config and override config from an environment variable
    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr.db'),
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default'
    ))

    app.config.from_envvar('FLASKR_SETTINGS', silent=True)


The `Config` object works similarly to a dictionary so we can update it with new values.


    def connect_db():
        """Connects to the specific database."""
        rv = sqlite3.connect(app.config['DATABASE'])
        rv.row_factory = sqlite3.Row
        return rv

    def get_db():
        """Opens a new database connection if there is none yet for the current application context.
        """
        if not hasattr(g, 'sqlite_db'):
            g.sqlite_db = connect_db()
        return g.sqlite_db

    @app.teardown_appcontext
    def close_db(error):
        """Closes the database again at the end of the request."""
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()
