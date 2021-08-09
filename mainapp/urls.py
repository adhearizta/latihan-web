from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile),
    path('example/', views.example),
    path('second/', views.second_page),
    path('', views.landing_page),
]
