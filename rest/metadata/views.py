from django.shortcuts import render
from metadata import serializers, models
from rest_framework import viewsets
from django_filters import rest_framework as filters


class LabelFilter(filters.FilterSet):
    label = filters.CharFilter(lookup_expr="icontains")


class DocumentFormatViewset(viewsets.ModelViewSet):
    queryset = models.DocumentFormat.objects.all()
    serializer_class = serializers.DocumentFormatSerializer
    filterset_class = LabelFilter


class DocumentSubjectSerializer(viewsets.ModelViewSet):
    queryset = models.DocumentSubject.objects.all()
    serializer_class = serializers.DocumentSubjectSerializer
    filterset_class = LabelFilter
