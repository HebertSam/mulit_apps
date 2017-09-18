from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = 'Hello these are your blogs'
    return HttpResponse(response)

def new(request, number):
    response = 'Hello this a user form placeholder {}'.format(number)
    return HttpResponse(response)