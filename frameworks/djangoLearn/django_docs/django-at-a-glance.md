# Django at a glance

Source: [Django Docs: Django at a glance](https://docs.djangoproject.com/en/1.10/intro/overview/)

**Why Django**

Django was designed to make web-development tasks fast and easy. 

---

## Design your model

Django comes with an [**object-relational mapper**](https://en.wikipedia.org/wiki/Object-relational_mapping). This means you describe your database layout in Python code.

**Location:** `mysite/news/models.py`

        from django.db import models

        # returning Reporter

        class Reporter(models.Model):
        full_name = models.CharField(max_length=70)

        def __str__(self):      # __unicode__ on Python 2
                return self.full_name

        # returning Article

        class Article(models.Model):
                pub_date = models.DateField()
                headline = models.CharField(max_length=200)
                content = models.TextField()
                reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

        def __str__(self):      # __unicode__ on Python 2
                return self.headline

### Install it

Run the Django command-line utility to create the database tables automatically:

        $ python manage.py migrate

The migrate command looks at all your available models and creates tables in your database for whichever tables don't already exist, as well as optionally providing much richer schema control.

---

### Some additional notes

#### Object-relational mapping

Object-relational mapping in computer science is a programming techique for converting data between imcopatible type systems in object-oriented programming languages. This creates, in effect, a "virtual object database" that can be used from within the programming language. These are both free and commercial packages available that perform object-relational mapping, although some programmers opt to construct their own ORM tools.

In object-oriented programming, data-management tasks act on object-oriented (OO) objects that are almost always scalar values. Blah, blah, blah...

The [**data-model syntax**](https://docs.djangoproject.com/en/1.10/topics/db/models/) offers many rich ways of representing models .

#### Models

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you're storing. Generally, each model maps to a single database table.

**The basics**:

 - Each model is a Python class that subclasses `django.db.models.Model`

 - Each attribute of the model represents a database field.

 - With all of this, Django gives you an automatically-generated database-access API; see Making queries.


**Example**

This model defines a Person, which has a `first_name` and a ` last_name`:

	from django.db import models

	class Person(models.Model):
		first_name = models.CharField(max_length=30)
		last_name = models.CharField(max_length=30)

`first_name` and `last_name` are fields of the model. Each field is specific as a class attribute, and each attribute maps to a database column.

The above **Person** model would create a database table like this:

	CREATE TABLE myapp_person (
		"id" serial NOT NULL PRIMARY KEY,
		"first_name" varchar(30) NOT NULL,
		"last_name" varchar(30) NOT NULL
	);

---

## Enjoy free API

With that, you get a free and rich, Python API to access your data. The API is created on the fly. No code generation necessary:

	# import the models we created from our "news" app
	>>>> from news.models import Reporter, Article

	# no reporters are in the system yet.
	>>>> Reporter.objects.all()
	<QuerySet []>

	# create a new Reporter.
	>>>> r = Reporter(full_name = 'John Smith')

	# save the object into the database. You have to call save() explicitly.
	>>>> r.save()

	# now it has an ID
	>>>> r.id
	1

	# now the reporter is in the database.
	>>>> Reporter.objects.all()
	<QuerySet [<Reporter: John Smith>]>

	# Fields are represented on the Python object.
	>>>> r.full_name
	'John Smith'

	# django provides a rick database lookup API.
	>>>> Reporter.objects.get(id=1)
	<Reporter: John Smith>
	>>>>
	Reporter.objects.get(full_name_startswith='John')
	<Reporter: John Smith>
	>>>>
	
	# --------- MISSING NOTES HERE ----------- #

---

## A dynamic admin interface: it's not just scaffolding - it's the whole house

Once your models are defined, Django can automatically create a professional, production ready **administrative interface** - a website that lets authenticated users add, change, and delete objects. 

**Location:** `mysite/news/models.py`

	from django.db import models
	
	class Article(models.Model):
		pub_date = models.DateField()
		headline = models.CharField(max_length = 200)
		content = models.TextField()
		reporter = models.ForeigmKey(Reporter, on_delete=models.CASCADE)

**Location:** `mysite/news/admin.py`

	from django.contrib import admin

	from . import models

	admin.site.register(models.Article)

The idea is that the site is edited by staff, or a client - without having to deal with creating a backend kjust to edit content. We focus, instead, on developing the way data is presented to the public.

---

## Design your URLs

A clean, elegant URL scheme is an important detail in a high-quality web application. Django encourages beautiful URL design.
	
To design URLs for your app, you create a Python module called a `URLconf`. A table of contents for your app, it contains a simple mapping between URL patterns and Python callback functions. URLconfs also server to decouple URLs from Python code.

Here is more documentation on [URLs](https://docs.djangoproject.com/en/1.10/topics/http/urls/).

Here is what a URLconf might look like for the **Reporter/Article** example:

**Location:** `mysite/news/urls.py`

	from django.conf.urls import url

	from . import views

	urlpatterns = [
		url(r'^articles/([0-9]{4})/$', views.year_archive),
		url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
		url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
	]

The code above maps URLs, as simple regular expressions, to the location of Python callback functions ("views"). The regular expressions use parenthesis to "capture" values from the URLs. When a user requests a page, Django runs through each pattern, in order, and stops at the first one that matches the requested URL. If no URL matches, Django calls a special-case 404 view. This is blazingly fast, because the regular expressions are compiledat load time.

Once one of the regexes matches, Django imports and calls the given view, which is a simple Python function. Each view gets passed a request object - which contains request metadata - and the values captured in the regex.

For example, if a user requested a URL `/articles/2005/05/399323/`, Django would call the function **news.views.article_detail(request, '2005', '05', '39323')**.

---

## Write your views

Each view is responsible for two things:

 1. Return HttpResponse object containing the content for the requested page

 2. Raise an exception such as Http404

The rest is up to you.

Generally, a view retrieves data according to the parameters, loads a template and renders the template with the retrieved data. Here is an example view for `year_archive` from above:

**Location:** `mysite/news/views.py`

	from django.shortcuts import render
	
	from .models import Article

	def year_archive(request, year):
		a_list = Article.objects.filter(pub_date__year=year)
		context = {'year': year, 'article_list': a_list}
		return render(request, 'news/year_archive.html', context)

This example uses Django's template system, which has several powerful features but strives to stay simple enough for non-programmers to use.

---

## Design your templates

The code above loads the `news/year_archive.html` template.

Django has a template search path, which allows you to minimize redundancy among templates. In your Django settings, you specify a list of directories to check for templates with [DIRS](https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-TEMPLATES-DIRS). If a template doesn't exist in the first directory, it checks the second, and so on.

Let's say the `news/year_archive.html` template was found. Here is what it would look like:

**Location:** `mysite/news/templates/news/year_archive.html`

	{% extends "base.html" %}

	{% block title %}Articles for {{ year }}{% endblock %}

	{% block content %}
	<h1>Articles for {{ year }}</h1>

	{% for article in article_list %}
		<p>{{ article.headline }}</p>
		<p>By {{ article.reporter.full_name }} </p>
		<p>Published {{ article.pub_date|date:"F j, Y" }}</p>
	{% endfor %}
	{% endblock %}

Variables are surrounded by double-curly braces. **`{{ article.headline }}`** means "Output" the value of the article's headline attribute." But dots aren't used only for attribute lookup. They also can do dictionary-key lookup, index lookup and function calls.

Note `** article.pub_date|date:"F j, Y" **` uses a Unix-style "pipe" (the "|" character). This is called a template filter, and it's a way to filter the value of a variable. In this case, the date filter formats a Python datetime object in the given format (as found in PHP's date function).

You can chain together as many filters as you'd like. You can also write custom template filters. You can write custom template tags, which run custom Python code behind the scenes.

Finally, DJango uses the concept of "template inheritance". That's why the {% extends "base.html" %} does. It means "First load the template called 'base', which has defined a bunch of blocks, and fill the blocks with the following blocks." In short, that let's you dramatically cut down on redundancy in templates: each template has to define only what's unique to that template.

Here is what the "base.html" template, including the use of static files, might look like:

**Location:** `mysite/templates/base.html`

	{% load static %}
	<html>
	<head>
		<title>{% block title %}{% endblock %}</title>
	</head>
	<body>
		<img src="{% static "images/sitelogo.png" %}" alt="Logo" />
		{% block content %}{% endblock %}
	</body>
	</html>



---

## This is just the surface

There are additional features to Django's functionality:

 - A caching framework that integrates with memchached or other backends.

 - A syndication framework that makes creating RSS and Atom feeds as easy as writing a small Python class.

 - More sexy automatically generated admin features = this overview barely scratched the surface.
