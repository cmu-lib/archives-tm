from rest_framework import serializers
from metadata import models


class RecordSerializer(serializers.ModelSerializer):
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
