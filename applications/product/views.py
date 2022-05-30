from rest_framework import viewsets
from applications.product.models import Product
from applications.product.serializers import ProductSerializer

"""test"""


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
