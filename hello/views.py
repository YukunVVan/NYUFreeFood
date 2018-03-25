from django.shortcuts import render
from django.http import HttpResponse

# from .models import Greeting

# Create your views here.
# def index(request):
#     # return HttpResponse('Hello from Python!')
#     return render(request, 'index.html')
#
#
# def db(request):
#
#     greeting = Greeting()
#     greeting.save()
#
#     greetings = Greeting.objects.all()
#
#     return render(request, 'db.html', {'greetings': greetings})

def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def product(request):
    return render(request, 'product.html')

def product2(request):
    return render(request, 'product2.html')

def product3(request):
    return render(request, 'product3.html')

def product4(request):
    return render(request, 'product4.html')

def playlist(request):
    return render(request, 'playlist.html')

def playlist2(request):
    return render(request, 'playlist2.html')
