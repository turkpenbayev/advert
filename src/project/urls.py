from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

import adverts.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/weekly-tests/', include(adverts.urls))
]

schema_view = get_schema_view(
    openapi.Info(
        title="Adverts API",
        default_version='v1',
        description=""
    ),
    public=True,
    permission_classes=(),
)

if settings.SHOW_DOCS:
    urlpatterns += [
        path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # adds nothing if not in DEBUG
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # adds nothing if not in DEBUG