from django.urls import path

from applications.about_us.views import HelpListView, NewsListView, AdvantagesListView, OfferListView, AboutListView

urlpatterns = [
    path('help/', HelpListView.as_view()),
    path('news/', NewsListView.as_view()),
    path('advantages/', AdvantagesListView.as_view()),
    path('offer/', OfferListView.as_view()),
    path('about', AboutListView.as_view()),
]