from rest_framework import serializers

from adverts.models import City, Category, Advert


class ListCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name',)
        read_only_fields = fields


class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)
        read_only_fields = fields


class AdvertSerializer(serializers.ModelSerializer):
    city = ListCitySerializer(read_only=True)
    category = ListCategorySerializer(read_only=True)

    class Meta:
        model = Advert
        fields = ('id', 'title', 'description', 'city', 'category', 'views', 'created')
        read_only_fields = fields