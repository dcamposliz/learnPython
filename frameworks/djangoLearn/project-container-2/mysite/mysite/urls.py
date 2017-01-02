from django.conf.urls import include, url
from django.contrib import admin

### IT'S NECESSARY TO IMPORT OTHER APPLICATION'S URLS
from polls import urls

#import pdb; pdb.set_trace();

urlpatterns = [
	### IT'S NECESSARY TO SPECIFY THE URL EXPECTED AS WELL AS THE NAMESPACE
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', admin.site.urls),
]

# include() allows for referencing other URLconfs

# url(regex, view, kwargs, name)
#	regex: the url entered by the user
#	view: the view returned by django
#	kwargs: don't know, and don't care
#	name: don't know yet, but probably care to learn
