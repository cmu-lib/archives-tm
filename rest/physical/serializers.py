from rest_framework import serializers
from physical import models


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Box
        fields = ["url", "id", "label", "sequence"]


class FolderSerializer(serializers.ModelSerializer):
    box = BoxSerializer()

    class Meta:
        model = models.Folder
        fields = ["url", "id", "label", "sequence", "box"]


class BundleSerializer(serializers.ModelSerializer):
    folder = FolderSerializer()

    class Meta:
        model = models.Bundle
        fields = ["url", "id", "label", "sequence", "folder"]


class DocumentSerializer(serializers.ModelSerializer):
    bundle = BundleSerializer()

    class Meta:
        model = models.Document
        fields = ["url", "id", "label", "sequence", "bundle", "pdf", "fulltext"]


class PageSerializer(serializers.ModelSerializer):
    document = DocumentSerializer()

    class Meta:
        model = models.Page
        fields = ["url", "id", "label", "sequence", "document", "image"]

