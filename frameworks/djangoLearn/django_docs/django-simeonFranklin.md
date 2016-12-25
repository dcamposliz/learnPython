# Overview of Django

Source: [Python Web Development: Understanding Django for Beginners](https://www.youtube.com/watch?v=zTNA0MtZwso)

Web application framework built in Python.

Released in 2005.

## Why Django

 - Docs

 - Python

 - Full-stack framework

Read https://docs.djangoproject.com/

Go do the django tutorial.

---

Django is HTTP in, HTTP out

---

## Projects

A web application is a project. Django comes with a tool to create a starting project for you.

	django-admin.py startproject PROJECT_NAME

A project contains:

 - `settings.py`: configuration for the project

 - `manage.py`: command runner

 - `urls.py`: starting point to configure urls

We can use `manage.py` to start up a development server to view our web app!

	python manage.py runserver

---

## Applications

A project is made of many applications.

Django includes many built in apps in `django.contrib` for authentication, serving static files, security. We need to create our own apps. The start page helpfully suggest we try:

	python manage.py startapp APP_NAME

Within `APP_NAME` we can find:

 - `views.py`

 - `__init__.py`

 - `tests.py`

 - `models.py`

We must edit our `settings.py` file to specify a database. It should look like this:

	DATABASES = {
		'default' : {
			'ENGINE' : 'django.db.backends.sqlite',
			'NAME' : 'storytime.sqlite3',
		}
	}

Do not use sqlite3 in production.

Need to add my new application to my `settings.py` file, within the `INSTALLED_APPS` directive:

	INSTALLED_APPS = (
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.sites',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		'APP_NAME'
	)

---

From this point on, we learn about 4 fundamental concepts:

 - URLs

 - Views

 - Models

 - Templates

---

# Fundamental Concept 1: `urls.py`

	from django.conf.urls import patterns, include, url

	urlpatterns = patterns('',
		# Examples:
		# url(r'^$', 'storytime.views.home', name='home'),
		# url(r'^storytime/', include('storytime.foo.urls')),
	)

`urls.py` requires us to learn **regex** patterns, which is particularly painful.

**A simple example**:

	from django.cong.urls import paterns, include, url

	urlpatterns = patterns('',
		url(r'^$', 'story.views.home', name='home')
	)

 - `url` is a function call that builds url patterns.

 - `^$` is the regex for "I didn't get nothing"

 - `story.views.home` is the Python import string to get to a view

 - the name of a url lets us figure out which urls go where later on

---

# Fundamental Concept #2: `views.py`

**HTTP Request** > **URLs** > **VIEWS [ MODELS , TEMPLATES ]** > **HTTP Response**

For example:

	from django.http import HttpResponse
	
	def home(request):
		return HttpResponse("Hello world!")

---

# Fundamental Concept #3: `templates`

 - If we want to make a web application, we better build a response that has some HTML

 - My application likely has a lot of `html` that does not change (the site design) and some that does

 - Most web frameworks include `template engines`

 - Basically `html` + `placeholders` that might be code 

---

**Base Template**

Let's make a base template with out "site design" in it.

	$ mkdir -p story/templates/story
	$ touch story/templates/story/base.html

---

### `base.html`

	<html>
	  <head>
	    <title>This is a webapp!</title>
	  </head>
	  <body>
	    <h1></h1>
	    {% block content %}
	    {% endblock %}
	  </body>
	</html>

Django template language provides `tags`, `filters`, and output.

---

**Template Inheritance**

Let's create another template called `home.html`.

---

### `home.html`

	{% extends "story/base.html" %}
	{% block content %}
	{{ hello }}
	{% endblock %}

---

 - `home.html` inherits from `base.html`. The `extends` block tag means `home.html` will be shown inside of `base.html`.

 - More specifically, any blocks in `home` will show up in the same named block in `base`

 - `{{ hello }}` will output the variable `hello` passed by the view

---

**Template Inheritance**

### `story/views.py`

	from django.shortcuts import render_to_response

	def home(request):
		return render_to_response("story/home.html", {'hello': "Hello World!"})

---

Learn about Template tags and filters!

if thens

loopings

for eachs

this is what most of the programming is anyway...

---







