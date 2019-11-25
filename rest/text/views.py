from django.shortcuts import render
from rest_framework import viewsets
from text import serializers, models
from physical.views import GetSerializerClassMixin
from rest_framework.decorators import action
from django_filters import rest_framework as filters


class TopicModelViewset(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = models.TopicModel.objects.all()
    serializer_class = serializers.TopicModelSerializer


class TopicViewset(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = models.Topic.objects.all()
    serializer_class = serializers.TopicDetailSerializer
    serializer_action_classes = {"list": serializers.TopicListSerializer}
