from rest_framework import serializers

from applications.collection.models import Collections, CollectionsImage


class CollectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collections
        fields = '__all__'


class CollectionsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CollectionsImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep


