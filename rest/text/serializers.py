from django import forms
from rest_framework import serializers
from text import models
from physical import models as physical_models
from physical.serializers import DocumentListSerializer
from django_filters import rest_framework as filters


class TopicFilter(filters.FilterSet):
    terms = filters.CharFilter()
    documents = filters.ModelChoiceFilter(
        queryset=physical_models.Document.objects.all()
    )
    log = filters.NumberFilter()


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = ["id", "url", "terms"]
        filterset_class = TopicFilter


class TopicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = ["id", "url", "topic_model", "terms"]


class TopicModelFilter(filters.FilterSet):
    documents = filters.ModelChoiceFilter(
        queryset=physical_models.Document.objects.all()
    )


class TopicModelSerializer(serializers.ModelSerializer):
    topics = TopicListSerializer(many=True, read_only=True)

    class Meta:
        model = models.TopicModel
        fields = [
            "id",
            "url",
            "n_topics",
            "topics",
            "n_topics",
            "chunksize",
            "passes",
            "iterations",
            "min_count",
            "no_above",
            "is_calculated",
        ]
        read_only_fields = ["created_model", "topics", "is_calculated"]


class DocumentTopicSerializer(serializers.ModelSerializer):
    document = DocumentListSerializer()

    class Meta:
        model = models.DocumentTopic
        fields = ["document", "topic", "log"]
