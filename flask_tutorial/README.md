# The Flask Tutorial

Flask is a micro-framework.

## Requirements

Flask depends on external libraries like `Werkzeug` (toolkit for `WSGI`, the standard Python interface between web applications and a variety of servers for both development and deployment environments) and `Jinga2` (a toolkit for rendering templates). We will also need **Python 2** and `virtualenv`.

**So, what are these different libraries?**

## Wekzeug

[Wekzeug Docs](http://werkzeug.pocoo.org/)

`Werkzeug` is a `WSGI` utility library for Python. It's widely used and licensed.

Werkzeug is simple.

    from werkzeug.wrappers import Request, response

    @Request.applications
    def application(request):
      return Response('Hello World!')

    if __name__ == '__main__':
      from werkzeug.serving import run_simple
      run_simple('localhost', 4000, application)

`Werkzeug` started as a simple collection of various utilities for `WSGI` applications and has become one of the most advanced `WSGI` utility modules. It includes a powerful debugger, fully featured request and response objects, HTTP dates, cookie handling, file uploads, a powerful URL routing system and a bunch of community contributed addon modules.

It does a Unicode and doesn't enforce a specific template engine, database adapter or anything else. It does not even enforce a specific way of handling requests and leaves all that up to the developer.

In the Box:

- HTTP header parsing and dumping
- Easy to use request and response objects
- Interactive JavaScript based in-browser debugger
- 100% WSGI 1.0 compatible
- Supports Python 2.6, 2.7, 3.3
- Unicode support
- Basic session and signed cookie support
- URI and IRI utilities with unicode awareness
- Built-in library of fixes for buggy WSGI servers and browsers
- Integrated routing system for matching URLs to endpoints and vice versa

**So, what template engine and database adapter do we use?**

## Jinga2

[Jinja2](http://jinja.pocoo.org/)

Jinga2 is a full featured template engine for Python. It has full Unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.

Jinja is Beatutiful.

    {% extends "layout.html" %}
    {% block body %}
      <ul>
        {% for user in users %}
          <li><a href="{{ user.url }}">{}</li>
        {% endfor %}
      </ul>
    {% endblock %}

`Jinga2` is one of the most used template engines for Python. It is inspired by Django's templating system but extends it with an expressive language that gives template authors a more powerful set of tools. On top of that it adds sandboxed execution and optional automating excaping for applications where security is important.

It is internally based on Unicode and runs on a wide range of Python versions from 2.4 to current versions including Python 3.

## virtualenv

#########################################
##    ADD SOME BASIC NOTES ON `virtualenv`
#########################################

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

Learn more about options for running apps in the [official Flask tutorial](http://flask.pocoo.org/docs/0.11/quickstart/).

# Running in Debug Mode

...

    export FLASK_DEBUG=1
    $ flask run

# Routing

...
