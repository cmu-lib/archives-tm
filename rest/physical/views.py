from rest_framework import viewsets
from physical import serializers
from physical import models


class BoxViewSet(viewsets.ModelViewSet):
    queryset = models.Box.objects.all()
    serializer_class = serializers.BoxSerializer


class FolderViewSet(viewsets.ModelViewSet):
    queryset = models.Folder.objects.all()
    serializer_class = serializers.FolderSerializer


class BundleViewSet(viewsets.ModelViewSet):
    queryset = models.Bundle.objects.all()
    serializer_class = serializers.BundleSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
