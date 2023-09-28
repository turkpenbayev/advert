from rest_framework import viewsets, mixins

from adverts.models import Advert
from adverts.serializers import AdvertSerializer


class AdvertViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AdvertSerializer

    def get_queryset(self):
        return Advert.objects.select_related('city', 'category')
