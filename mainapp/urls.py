from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile),
    path('shop/', views.shop),
    path('example/', views.example),
    path('secondpage/', views.secondpage),
    path('firstpage/', views.firstpage),
    path('home/', views.home),
    path('shopsuamilist/', views.shopsuamilist),
]
