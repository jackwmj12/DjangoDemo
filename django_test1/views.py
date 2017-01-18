from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("&lt;p&gt;Hello World&lt;/p&gt;")

# Create your views here.
