from django.http import HttpResponse
from django.shortcuts import render

# Creating our views here.
def aboutMe(request):
    return HttpResponse("Hello it's me Dinesh!!")

def aboutYou(request, name):
    return HttpResponse(f"Ohh! you are {name}")

def add(request, num1, num2):
    return HttpResponse(f"Total is {num1+num2}")