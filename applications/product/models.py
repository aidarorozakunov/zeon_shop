from django.db import models
from uuslug import slugify
from applications.collection.models import Collections
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField


class Product(models.Model):
    title = models.CharField(max_length=255, null=True)
    collections = models.ForeignKey(Collections, null=True, on_delete=models.SET_NULL, related_name='product')
    article = models.CharField(max_length=150)
    description = RichTextField()
    size_range = models.CharField(max_length=150)
    compound = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField(default=1)
    material = models.CharField(max_length=150)
    hit = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    price = models.IntegerField(null=True)
    sales = models.IntegerField(null=True)
    price_sales = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.sales:
            self.price_sales = self.price - (self.price/100) * self.sales
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image', null=True)
    image = models.ImageField(upload_to='')
    color = ColorField(format="hexa")

    def __str__(self):
        return self.product.title


class Slider(models.Model):
    link = models.TextField(null=True)

    def __str__(self):
        return self.link


class SliderImage(models.Model):
    image = models.ImageField(upload_to='')
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='image', null=True)

    def __str__(self):
        return self.slider.link
