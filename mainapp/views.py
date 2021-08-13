from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def landing_page(request):
    return HttpResponse("INI BUKAN NURI INI DHEa asli")


def second_page(request):
    return HttpResponse("SecondPage")


def profile(request):
    return HttpResponse('My Profile')


def count(request, angka):
    angka = angka+1
    return HttpResponse(str(angka))


def sapa(request, nama):
    return HttpResponse("halo "+nama)


def example(request):
    return render(request, 'example.html')


def shop(request):
    return render(request, 'shop.html')


def firstpage(request):
    return render(request, "firstpage.html")


def secondpage(request):
    return render(request, "secondpage.html")


def home(request):
    return render(request, "home.html")


def shopsuamilist(request):
    # try:
    print(request.GET)
    category_suami = Category.objects.get(pk=1)
    product_bermasalah = Product.objects.filter(category=category_suami).filter(
        name__contains=request.GET['product_name'])
    if(product_bermasalah.count() != 0):
        return render(request, 'shopsuamilist.html', {'product_list': product_bermasalah, "available": True})
    else:
        return render(request, 'shopsuamilist.html', {'available': False})
    # except:
    return HttpResponse("kasian error :(")
