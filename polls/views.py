from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is Jacob debbarma, Inspector T.W Department.")


#templateview
class Homeview(TemplateView):
	template_name = 'polls/home.html'