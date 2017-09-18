from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = 'Hello these are your blogs'
    return HttpResponse(response)

def new(request, number):
    response = 'Hello this a blog form placeholder {}'.format(number)
    return HttpResponse(response)

def create(request):
    return redirect('blog/')

def show(request, number):
    response = 'to display blog number {}'.format(number)
    return HttpResponse(response)

def edit(request, number):
    response = 'edit blog number {}'.format(number)
    return HttpResponse(response)

def delete(request, number):
    response = 'delete blog number {}'.format(number)
    return HttpResponse(response)