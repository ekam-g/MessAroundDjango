from django.shortcuts import render


def home(request):
    print("Home Page Requested")
    return render(request, 'home.html')


def data(request):
    print("Data Page Requested")
    return render(request, 'databaseUse.html')
