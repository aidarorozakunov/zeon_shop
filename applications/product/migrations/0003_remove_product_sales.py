# Generated by Django 4.0.4 on 2022-05-27 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productimage_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sales',
        ),
    ]
