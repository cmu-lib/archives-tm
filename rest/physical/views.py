from django import forms
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from physical import serializers, models
from django_filters import rest_framework as filters
from text import models as text_models
from metadata import models as metadata_models


class GetSerializerClassMixin(object):
    def get_serializer_class(self):
        """
        A class which inhertis this mixins should have variable
        `serializer_action_classes`.
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:
        class SampleViewSet(viewsets.ViewSet):
            serializer_class = DocumentSerializer
            serializer_action_classes = {
               'upload': UploadDocumentSerializer,
               'download': DownloadDocumentSerializer,
            }
            @action
            def upload:
                ...
        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.
        """
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class BoxViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = models.Box.objects.all()
    serializer_class = serializers.BoxDetailSerializer
    serializer_action_classes = {"list": serializers.BoxListSerializer}


class FolderViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = models.Folder.objects.all()
    serializer_class = serializers.FolderDetailSerializer
    serializer_action_classes = {"list": serializers.FolderListSerializer}


class BundleViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = models.Bundle.objects.all()
    serializer_class = serializers.BundleDetailSerializer
    serializer_action_classes = {"list": serializers.BundleListSerializer}


class DocumentFilter(filters.FilterSet):
    topic_model = filters.ModelChoiceFilter(
        queryset=text_models.TopicModel.objects.all(),
        field_name="topic_models",
        widget=forms.TextInput,
    )
    document_format = filters.ModelChoiceFilter(
        queryset=metadata_models.DocumentFormat.objects.all(),
        field_name="record__document_format",
    )
    document_subject = filters.ModelChoiceFilter(
        queryset=metadata_models.DocumentSubject.objects.all(),
        field_name="record__document_subject",
    )
    label = filters.CharFilter(lookup_expr="icontains")
    topics = filters.ModelChoiceFilter(queryset=text_models.Topic.objects.all())


class DocumentViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentDetailSerializer
    serializer_action_classes = {"list": serializers.DocumentListSerializer}
    filterset_class = DocumentFilter


class PageViewSet(viewsets.ModelViewSet):
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
