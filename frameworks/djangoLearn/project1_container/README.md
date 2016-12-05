# Django App with Python3 and virtualenv

Source: [Introduction - Django Web Development with Python 1 by sentdex](https://youtu.be/FNQxxpM1yOs)

---

To execute, enter in terminal:

	python manage.py runserver

Make sure to be running `virtualenv`.

---

# About our files

`pwd: project1_container`

`theProject/theProject/settings.py` is one of our most important files.

It contains our `INSTALLED_APPS` application definition. It contains our `SECRET_KEY`, which should be kept secret, and gives us admin priviledges. If stolen, our sessions could be de-crypted, rendering our app vulnerable.

`project1_container/theProject/theProject/urls.py` is kind of the main controller of the website. It contains our urlPatterns, which are built with regular expressions.

**webapp**

`pwd: project1_container/theProject/webapp`

`webapp` is our first standalone micro-app directory. Django apps are a collection of micro-apps glued together and routed in the Django-way; it's awesome for simplifying development.

**tests**

`webapp/tests.py`

`tests.py` is where we put our tests, for each micro-app. Tests are a way of sanitizing code, it tests functionality of code injections, including how it integrates to the rest of the base code. Testing will run each new feature at given parameters, saving time in terms of manual validation.

**views**

`webapp/views.py`

`views.py` are what the user sees.

**urls**

`webapp/urls.py`

`urls.py` are what glues the rest of the application together. 

**models**

`webapp/models.py`

We also have `models.py`, which is our way of handing data and Django's way of handling databases for us.

---

# Making an App

Within `project1_container/theProject` we run:

	python manage.py startapp webapp

Where `webapp` is a name of our choosing. This could have been called `blog`, `projects`, `store`, etc.

We want to put `webapp` within our `INSTALLED_APPS` array in our `project1_container/theProject/theProject/settings.py` file, as this incorporates our micro-app into our 'app hub'.
