from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=CASCADE)

# cascade itu buat kalo apus satu field, field lain juga diapus


class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    review = models.TextField()
    product = models.ForeignKey(Product, on_delete=CASCADE)


# class karyawan(models.Model):
#     id_karyawan = models.CharField(max_length=100, primary_key= True)
