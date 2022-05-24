from django.urls import path
from applications.product.views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),
]