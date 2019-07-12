from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello world</h1>")
	my_context = {
		"my_text": "This is home page"
	}
	return render(request, 'home.html', my_context)


def contact_view(request, *args, **kwargs):
	return HttpResponse("<h1>Hello Contacts</h1>")