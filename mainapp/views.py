from django.shortcuts import render
from django.http import HttpResponse


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
