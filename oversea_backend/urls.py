from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.views.generic import RedirectView
from rest_framework import routers
from rest_framework import permissions

from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    # path('', RedirectView.as_view(url='/user/intro', permanent=False)),
    path("admin/", admin.site.urls),
    path("user/", include("users.urls")),
    path("store/", include("store.urls")),
    path("chat/", include("chat.urls")),
    path("restaurant/", include("restaurant.urls")),
    path("", include_docs_urls(title="OverSea API")),
    path(
        "schema",
        get_schema_view(
            title="OverSea API",
            description="API for the Humascot OverSea",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
]
