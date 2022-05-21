from django.shortcuts import render


def home(request):
    print("Home Page Requested")
    return render(request, 'home.html')
