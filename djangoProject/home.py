from django.shortcuts import render
from django import forms


def home(request):
    print("Home Page Requested")
    return render(request, 'home.html')


def data(request):
    print("Data Page Requested")
    return render(request, 'databaseUse.html')


def int(request):
    print("Initial Page Requested")
    return render(request, 'home.html')
