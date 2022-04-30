from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HTTPResponse('home')

def training(request):
    return HTTPResponse('training')

def players(request):
    return HTTPResponse('players')