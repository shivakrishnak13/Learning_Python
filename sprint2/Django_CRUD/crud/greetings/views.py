from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request) :
    return HttpResponse("Welcome to the My First Django App")

def greet(request,username) :
    return HttpResponse(f"Hello {username}..")

def farewell(request,username) :
    return HttpResponse(f"{username}, Good Bye!")