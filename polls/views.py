from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #first we create the funcionality, and then create the connection
    #the connections are the url's,
    # there live all connections that activate our functionalities  
    return HttpResponse('Hello, world. You\'re at the polls index')
