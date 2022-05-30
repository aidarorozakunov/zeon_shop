from django.urls import path, include
# from applications.product.views import ProductListView, ProductDetailView
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()

router.register('product', ProductViewSet)
#
urlpatterns = [
    path('', include(router.urls)),

]
