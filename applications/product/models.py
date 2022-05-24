from django.db import models
from applications.collection.models import Collections
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField

class Product(models.Model):
    title = models.CharField(max_length=255)
    collections = models.ForeignKey(Collections, null=True, on_delete=models.SET_NULL, related_name='product')
    description = RichTextField()
    color = ColorField(format="hexa")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='products_photo')

    def __str__(self):
        return self.product.title
