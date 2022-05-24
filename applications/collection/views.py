from rest_framework import generics

from applications.collection.models import Collections
from applications.collection.serializers import CollectionsSerializer


class CollectionsListView(generics.ListAPIView):
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer
