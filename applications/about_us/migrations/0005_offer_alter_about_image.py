# Generated by Django 4.0.4 on 2022-05-26 09:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0004_advantages_advantagesimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('offer', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
