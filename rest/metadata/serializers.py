from rest_framework import serializers
from metadata import models


class RecordSerializer(serializers.ModelSerializer):
    document_format = serializers.SlugField("label")
    document_subject = serializers.SlugField("label")

    class Meta:
        model = models.DocumentRecord
        fields = [
            "label",
            "document_format",
            "document_subject",
            "created_date_text",
            "coverage_text",
            "document_subject_text",
        ]


class DocumentFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DocumentFormat
        fields = ["id", "label"]


class DocumentSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DocumentSubject
        fields = ["id", "label"]
