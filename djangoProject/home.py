from django.shortcuts import render


def home(request):
    print("fard")
    return render(request, 'templates/home.html')
