
from django.urls import path, include
from django.urls import path, re_path
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="school API",
        default_version='v1',
        description=" API For school",

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("school.urls")),


    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('documentation_swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
     path('documentation_redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]




