from django.urls import path

from applications.about_us.views import AboutListView, HelpListView, NewsListView, AdvantagesListView

urlpatterns = [
    path('', AboutListView.as_view()),
    path('help/', HelpListView.as_view()),
    path('news/', NewsListView.as_view()),
    path('advantages', AdvantagesListView.as_view())
]