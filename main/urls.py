from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls
from shorturl.views import ShortURLRedirectViewSet


api_urlpatterns = [
    path("", include("shorturl.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include((api_urlpatterns, "api"))),
    path("docs/", include_docs_urls(title="Short-URL API",)),
    path(
        "<str:shortURLstr>",
        ShortURLRedirectViewSet.as_view({"get": "self"}),
        name="user-detail",
    ),
]
