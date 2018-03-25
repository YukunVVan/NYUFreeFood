from django.shortcuts import render

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
