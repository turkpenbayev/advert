from django.db.models import F
from rest_framework import viewsets, mixins
from rest_framework import filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from adverts.models import Advert
from adverts.serializers import AdvertSerializer


class AdvertViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AdvertSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('city', 'category')
    search_fields = ["title", "description",]

    def get_queryset(self):
        return Advert.objects.select_related('city', 'category')

    def retrieve(self, request, pk, *args, **kwargs):
        Advert.objects.filter(pk=pk).update(views=F('views')+1)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
