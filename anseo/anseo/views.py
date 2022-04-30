from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('home')

def training(request):
    return HttpResponse('training')

def players(request):
    return HttpResponse('players')