from rest_framework import generics

from applications.about_us.models import About, Help, News
from applications.about_us.serializers import AboutSerializer, HelpSerializer, NewsSerializer, AdvantagesSerializer


class AboutListView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class HelpListView(generics.ListAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class AdvantagesListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = AdvantagesSerializer
