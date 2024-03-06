from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import path

schema_view = get_schema_view(
    openapi.Info(
        title="Notes API",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
