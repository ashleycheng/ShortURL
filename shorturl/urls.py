# from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"short_url", views.CreateShortURLViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
