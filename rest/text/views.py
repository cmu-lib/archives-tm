from django.shortcuts import render
from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from text import serializers, models
from physical.models import Document
from physical.views import GetSerializerClassMixin, DocumentFilter
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from text.tasks import generate_model


class TopicModelViewset(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = models.TopicModel.objects.all()
    serializer_class = serializers.TopicModelSerializer

    @action(detail=True, methods=["post"])
    def load_model(self, request, pk=None):
        tm = self.get_object()
        # Submit the query parameters as a JSON object
        filtered_documents = DocumentFilter(
            self.request.POST, queryset=Document.objects.all()
        ).qs
        doc_count = filtered_documents.count()
        if doc_count > 0:
            tm.documents.set(filtered_documents)
            tm.save()
            generate_model(tm)
            return Response({"id": tm.id, "docs_added": doc_count})
        else:
            return Response(
                {"non_field_error": "Filter returned 0 documents."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @transaction.atomic
    @action(detail=True, methods=["post"])
    def clear(self, request, pk=None):
        tm = self.get_object()
        doc_count = tm.documents.count()
        tm.documents.clear()
        return Response({"id": tm.id, "docs_added": doc_count})


class TopicFilter(filters.FilterSet):
    topic_model = filters.ModelChoiceFilter(
        queryset=models.TopicModel.objects.all(), field_name="topic_model"
    )
    terms = filters.CharFilter(lookup_expr="icontains")


class TopicViewset(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = models.Topic.objects.all()
    serializer_class = serializers.TopicDetailSerializer
    serializer_action_classes = {"list": serializers.TopicListSerializer}
    filterset_class = TopicFilter


class DocumentTopicFilter(filters.FilterSet):
    topic = filters.ModelChoiceFilter(queryset=models.Topic.objects.all())
    document = filters.ModelChoiceFilter(queryset=Document.objects.all())


class DocumentTopicViewset(viewsets.ModelViewSet):
    queryset = models.DocumentTopic.objects.order_by("log").distinct()
    serializer_class = serializers.DocumentTopicSerializer
    filterset_class = DocumentTopicFilter
