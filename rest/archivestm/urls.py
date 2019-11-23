from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from physical import views as physical_views

router = routers.DefaultRouter()
router.register(r"boxes", physical_views.BoxViewSet)
router.register(r"folders", physical_views.FolderViewSet)
router.register(r"bundles", physical_views.BundleViewSet)
router.register(r"documents", physical_views.DocumentViewSet)
router.register(r"pages", physical_views.PageViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
]
