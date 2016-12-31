# Django App with Python3 and virtualenv

## Source: [Introduction - Django Web Development with Python 1](https://youtu.be/FNQxxpM1yOs)

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

## Source: [Introduction - Django Web Development with Python 2](https://www.youtube.com/watch?v=iZ5my3krEVM&t=5s)

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

# Deleting `webapp`

We deleted webapp from `project1_container/theProject` because that's not what our app will be about.

For this, we remove the `webapp` `urlpattern` from `project1_container/theProject/theProject/urls.py`.

We also remove the `webapp` directory from the `project1_container/t
heProject/` directory.

---

## Source: [Jinja Templating - Django Web Development with Python 3](https://www.youtube.com/watch?v=3tf8XlhsQAo&t=2s)

# Making an App called `personal`

We are going to build an app about ourselves, called `personal`.

Within `project1_container/theProject` we ran:

	python manage.py startapp personal

Where `personal` is a name of our choosing. This could have been called `blog`, `projects`, `store`, etc.

We want to put `webapp` within our `INSTALLED_APPS` array in our `project1_container/theProject/theProject/settings.py` file, as this incorporates our micro-app into our 'app hub'.

--

## urls

We make `urls.py`. Of course, we do this within the `personal` directory; check its code, for reference. We also make sure to include in the main `urls.py` file.

--- 

## `templates` : [ `header.html` , `home.html` , `includes` : [ `snippet.html` ] ]

We create these files/directories within `personal` and proceed to write code. Check it :)

---

## Source: [Bootstrap HTML CSS - Django Web Development with Python 4](https://www.youtube.com/watch?v=p8qpu9WscFU&t=74s)

## `static`

To add nice UI/UX, we create a `static` directory within `personal`. There, we dump the contents of **bootstrap**, specifically, the `css`, `js`, and `fonts` directories. We add a `README.md` for context.

We want to load the bootstrap stuff in the `header.html`.
