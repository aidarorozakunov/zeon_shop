from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status, viewsets
from django_filters import rest_framework
from rest_framework.pagination import PageNumberPagination
from applications.product.models import Product
from applications.product.serializers import ProductSerializer


# class ProductPriceFilter(rest_framework.FilterSet):
#     min_price = rest_framework.NumberFilter(field_name='price',
#                                             lookup_expr='gte')
#     max_price = rest_framework.NumberFilter(field_name='price',
#                                             lookup_expr='lte')
#     class Meta:
#         model = Product
#         fields = [
#             'min_price',
#             'max_price',
#             'collections',
#         ]

#
# class ProductListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # pagination_class = PageNumberPagination
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filter_class = ProductPriceFilter
    # search_fields = ['title', ]

    # def get_serializer_context(self):
    #     return {'request': self.request}

#
# class ProductDetailView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#
# class FavoriteView(APIView):
#     permission_classes = [IsAuthenticated, ]
#
#     def get(self, request, pk):
#         profile = Profile.objects.get(user=request.user.id)
#         if profile.favorite.filter(id=pk).exists():
#             profile.favorite.set(profile.favorite.exclude(id=pk))
#             msg = 'Product was  deleted from favorites!'
#         else:
#             profile.favorite.add(pk)
#             profile.save()
#             msg = 'Product added to favorite successfully!'
#         return Response(msg, status=status.HTTP_200_OK)



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
