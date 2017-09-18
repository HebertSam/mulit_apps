from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = 'Hello these are your blogs'
    return HttpResponse(response)

def new(request):
    response = 'Hello this a blog form placeholder'
    return HttpResponse(response)
