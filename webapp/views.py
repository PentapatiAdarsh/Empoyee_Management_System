

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, request

from .models import *
import random as r



# Creating a views here.
def homepage(request):
    return render(request, 'index.html')

