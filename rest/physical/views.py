from rest_framework import viewsets
from physical import serializers
from physical import models


class BoxViewSet(viewsets.ModelViewSet):
    queryset = models.Box.objects.all()

