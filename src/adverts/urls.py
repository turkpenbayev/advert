from django.urls import path
from rest_framework.routers import SimpleRouter

from adverts.views import AdvertViewSet

router = SimpleRouter()
router.register('adverts', AdvertViewSet, basename='adverts')

urlpatterns = [
    *router.urls
]