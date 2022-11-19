from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
import requests
from requests.exceptions import HTTPError


def home(request):
    return render(request, 'index.html')



class CallbackView(TemplateView):
    template_name = "callback.html"
