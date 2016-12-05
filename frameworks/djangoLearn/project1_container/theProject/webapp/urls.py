from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index') # this is an index, begins and ends, has nothing in it; returns `views.index`
]

# added urls from django
# added views from .
# added url for index, which returns `views.index`, and whose namespace is 'index'
