from django.db import models
from ckeditor.fields import RichTextField


# class About(models.Model):
#     image = models.ImageField(upload_to='')
#     title = models.CharField(max_length=150)
#     description = RichTextField()
#
#     def __str__(self):
#         return self.title
#
#
# class AboutImage(models.Model):
#     about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about')
#
#     def __str__(self):
#         return self.about.title


class Help(models.Model):
    image = models.ImageField(upload_to='')
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class HelpImage(models.Model):
    help = models.ForeignKey(Help, on_delete=models.CASCADE, related_name='help')


class News(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    text = RichTextField()

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.news.title


class Advantages(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class AdvantagesImage(models.Model):
    advantages = models.ForeignKey(Advantages, on_delete=models.CASCADE, related_name='advantages')

    def __str__(self):
        return self.advantages.title


class Offer(models.Model):
    title = models.CharField(max_length=50)
    offer = RichTextField()

    def __str__(self):
        return self.title


class About(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=50)
    text = RichTextField()

    def __str__(self):
        return self.title


class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about')

    def __str__(self):
        return self.about.title