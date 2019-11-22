from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from physical import views

router = routers.DefaultRouter()
router.register(r"boxes", views.BoxViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
