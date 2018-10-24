from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
from django.contrib import messages
from django.utils.crypto import get_random_string
import random
# the index function is called when root is visited

def index(request):
    request='Hello World'
    return HttpResponse(request)


    