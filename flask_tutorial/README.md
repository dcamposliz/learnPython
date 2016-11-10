# The Flask Tutorial

Flask is a micro-framework.

## Requirements

Flask depends on external libraries like `Werkzeug` (toolkit for `WSGI`, the standard Python interface between web applications and a variety of servers for both development and deployment environments) and `Jinga2` (a toolkit for rendering templates). We will also need **Python 2** and `virtualenv`.

**So, what are these different libraries?**

## What is `wekzeug`?

[Wekzeug Docs](http://werkzeug.pocoo.org/)

`werkzeug` is a `WSGI` utility library for Python. It's widely used and licensed.

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

## What is Jinga2?

[Jinja2 Docs](http://jinja.pocoo.org/)

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

## What is `virtualenv`

[`virtualenv` Docs](https://virtualenv.pypa.io/en/stable/)

`virtualenv` is a tool to create **isolated** Python environments.

The basic problem being addressed is one of dependencies and versions, and indirectly permissions. Imagine you have an application that needs version 1 of some library, but another application requires version 2. It's easy to end up in a situation where you unintentionally upgrade an application that shouldn't be upgraded.

`virtualenv` creates an environment that has its own installation directories, that doesn't share libraries with other virtualenv environments.

## Install Dependencies

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

If you enable debug mode then the server will reload itself on code changes; it will also provide you with a helpful debugger if things go wrong.

    export FLASK_DEBUG=1
    $ flask run

# Routing

Modern web applications have beautiful URLs. This helps people remember the URLs, which is especially handy for applications that are used from mobile devices with slower network connections.

The `route()` decorator is used to bind a function to a URL. Here are some basic examples:

    @app.route(/)
    def index():
      return 'Index Page'

    @app.route('/hello')
    def hello():
      return 'Hello, World'

You can make certain parts of the URL dynamic and attach multiple rules to a function.

# Variable Rules

To add variable parts to a URL you can mark these special sections as <variable_name>. Such a part is then passed as a keyword argument to your function. Optionally a converter can be used by specifying a rule with <converter:variable_name>. Here are some examples:

    @app.route('/user/<username>')
    def show_user_profile(username):
      # show the user profile for that user
      return 'User %s' % username

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
      # show the post with the given id, the id is an integer
      return 'Post %d' % post_id

The following converters exist:

 - `string`: accepts any test without a slash (the default)

 - `int`: accepts integers

 - `float`: like `int` but for floating point values

 - `path`: like the default but also accepts slashes

 - `any`: matches one of the items provided

 - `uuid`: accepts UIID strings

# Unique URLs / Redirection Behavior

Flask's URL riles are based on Werkzeug's routing module. The idea is to ensure beautiful and unique URLs based on precedents laid down by Apache and earlier HTTP servers.

Take these two rules for example:

**Rule 1:**

    @app.route('/projects/')
    def projects():
      return 'The Project Page'

**Rule 2:**

    @app.route('/about')
    def about():
      return 'The About Page'

The two rules look rather similar, except for the trailing slash `/` in the URL definition.

Rule 1, the canonical URL for projects endpoint looks like a folder filesystem. Accessing it without the slash `/` will cause Flask to redirect to the canonical URL with the trailing slash.

In the second case, the URL is defined without the trailing slash, like the pathname of a file on UNIX-like systems. Accessing the URL with a trailing slash `/` will produce a 404 "Not Found" error.

This behavior allows relative URLs to continue working even if the trailing slash is omitted, consistent with how Apache and other servers work. Also, the URLs will stay unique, which helps search engines avoid indexing the same page twice.

# URL Building

...

    from flask import Flask, url_for
    app = Flask(__name__)
    @app.route('/')
    def index(): pass

    ...

    @app.route('/login')
    def login(): pass

    ...

    @app:route('/user/<username>')
    def profile(username): pass

    ...

    with app.test_request_context():
      print url_for('index')
      print url_for('login')
      print url_for('login', next='/')
      print url_for('profile', username='John Doe')

...

# HTTP Methods
