# The Flask Tutorial

Flask is a microframework.

## Requirements

Flask depends on external libraries like `Werkzeug` (toolkit for `WSGI`, the standard Python interface between web applications and a variety of servers for both development and deployment environments) and `Jinga2` (a toolkit for rendering templates).

We will also need Python 2.x and `virtualenv`. Google how to to install Python 2, if you haven't, already.

Install `virtualenv`:

    sudo pip install virtualenv

Install `Flask` globally:

    sudo pip install Flask

Maybe do upgrade your pip setup tools:

    pip2 install --upgrade pip setuptools

# Running Apps in Dev

Say you just saved your Flask app as `hello.py`, and are trying to run it in your development environment. Make sure to be in the same directory where your `hello.py` file lives (within your command line), and run the following commands:

    export FLASK_APP=hello.py
    flask run

Learn more about options for running apps in the [official Python tutorial](http://flask.pocoo.org/docs/0.11/quickstart/).

# Running in Debug Mode

...

    export FLASK_DEBUG=1
    $ flask run

# Routing

...
