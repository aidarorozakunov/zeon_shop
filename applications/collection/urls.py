from django.urls import path

from applications.collection.views import CollectionsListView

urlpatterns = [
    path('list/', CollectionsListView.as_view()),
]
