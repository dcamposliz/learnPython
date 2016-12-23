# Django at a glance

**Why Django**

Django was designed to make web-development tasks fast and easy. 



## Design your model

	from django.db import models
	
	# some more models code...

Django comes with an [**object-relational mapper**](https://en.wikipedia.org/wiki/Object-relational_mapping). This means you describe your database layout in Python code.

**Object-relational mapping**

Object-relational mapping in computer science is a programming techique for converting data between imcopatible type systems in object-oriented programming languages. This creates, in effect, a "virtual object database" that can be used from within the programming language. These are both free and commercial packages available that perform object-relational mapping, although some programmers opt to construct their own ORM tools.

In object-oriented programming, data-management tasks act on object-oriented (OO) objects that are almost always scalar values. Blah, blah, blah...

The [**data-model syntax**](https://docs.djangoproject.com/en/1.10/topics/db/models/) offers many rich ways of representing models .

### Models

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you're storing. Generally, each model maps to a single database table.

The basics:

 - Each model is a Python class that subclasses `django.db.models.Model`

 - Each attribute of the model represents a database field.

 - With all of this, Django gives you an automatically-generated database-access API; see Making queries.


Quick example: this model defines a Person, which has a `first_name` and a ` last_name`:

	from django.db import models

	class Person(models.Model):
		first_name = models.CharField(max_length=30)
		last_name = models.CharField(max_length=30)

`first_name` and `last_name` are fields of the model. Each field is specific as a class attribute, and each attribute maps to a database column.




It solves years' worth of database-schema problems. Here is a quick example:

	from django.db import models

	# returning Reporter

	class Reporter(models.Model):
	full_name = models.CharField(max_length=70)

	def __str__(self):	# __unicode__ on Python 2
		return self.full_name

	# returning Article

	class Article(models.Model):
		pub_date = models.DateField()
		headline = models.CharField(max_length=200)
		content = models.TextField()
		reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

	def __str__(self):	# __unicode__ on Python 2
		return self.headline	

---

## Install it

Run the Django command-line utility to create the database tables automatically:

	python manage.py migrate

The migrate command looks at all your available models and creates tables in your database for whichever tables don't already exist, as well as optionally providing much richer schema control.

--

## Enjoy free API

	from news.models import Reporter, Article

	# some more API stuff...

## A dynamic admin interface: it's not just scaffolding - it's the whole house

### `models.py`

	mysite/news/models.py

	from django.db import models
	
	class Article(models.Model):
		pub_date = models.DateField()
		headline = models.CharField(max_length = 200)
		content = models.TextField()
		reporter = models.ForeigmKey(Reporter, on_delete=models.CASCADE)

### `admin.py`

	mysite/news/admin.py

	from django.contrib import admin

	from . import models

	admin.site.register(models.Article)

## Design your URLs

## Write your views

## Design your templates

## This is just the surface

There is a
