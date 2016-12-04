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

It contains our `INSTALLED_APPS` application definition. It contains our `SECRET_KEY`, which should be kept secret, and gives us admin priviledges. If stolen our app can get hacked.

`project1_container/theProject/theProject/urls.py` is kind of the main controller of the website. It contains our urlPatterns, which are built with regular expressions.

---

# Making an App

Within `project1_container/theProject` we run:

	python manage.py startapp webapp

Where `webapp` is a name of our choosing.