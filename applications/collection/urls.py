from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from applications.collection.views import CollectionsListView
from applications.collection.views import CollectionViewSet

router = DefaultRouter()

router.register('product', CollectionViewSet)
#
urlpatterns = [
    path('', include(router.urls)),
]
