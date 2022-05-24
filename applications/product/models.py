from django.db import models
# from django.forms import CheckboxSelectMultiple

from applications.collection.models import Collections
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField

class Product(models.Model):
    title = models.CharField(max_length=255, null=True)
    collections = models.ForeignKey(Collections, null=True, on_delete=models.SET_NULL, related_name='product')
    color = ColorField(format="hexa")
    article = models.CharField(max_length=150)
    price = models.IntegerField(null=True)
    old_price = models.IntegerField(null=True)
    sales = models.IntegerField(null=True)
    description = RichTextField()
    size_range = models.CharField(max_length=150)
    compound = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField(default=1)
    material = models.CharField(max_length=150)
    hit = models.BooleanField(default=False)
    new = models.BooleanField(default=False)


    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='products_photo')

    def __str__(self):
        return self.product.title
