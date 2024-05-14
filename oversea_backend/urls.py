from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.views.generic import RedirectView
from rest_framework import routers
from rest_framework import permissions
# from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view


router = routers.DefaultRouter()
schema_view = get_schema_view(
    openapi.Info(
        title="Humascot API",
        default_version="v3",
        description="Humascot Test API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', RedirectView.as_view(url='/user/intro', permanent=False)),
    path("admin/", admin.site.urls),
    path("user/", include("users.urls")),
    path("store/", include("store.urls")),
    path("chat/", include("chat.urls")),
    path("restaurant/", include("restaurant.urls")),
    path("docs/", include_docs_urls(title='BlogAPI')),
    
    path('schema', get_schema_view(
        title="BlogAPI",
        description="API for the BlogAPI",
        version="1.0.0",
    ), name='openapi-schema'),
]

