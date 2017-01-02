Edited `polls/views.py`:

	from django.http import HttpResponse


	Def index(request):
		return HttpResponse("Hello, world. You're at the polls index.")


