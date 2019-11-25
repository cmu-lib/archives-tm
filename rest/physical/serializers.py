from rest_framework import serializers
from physical import models


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Page
        fields = ["url", "id", "label", "sequence", "image"]


class BoxListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Box
        fields = ["url", "id", "label", "sequence"]


class FolderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Folder
        fields = ["url", "id", "label", "sequence"]


class DocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Document
        fields = ["url", "id", "label", "sequence", "pdf", "n_pages"]


class BundleListSerializer(serializers.ModelSerializer):
    documents = DocumentListSerializer(many=True)

    class Meta:
        model = models.Bundle
        fields = ["url", "id", "label", "sequence", "documents"]


class BoxDetailSerializer(serializers.ModelSerializer):
    folders = FolderListSerializer(many=True)

    class Meta:
        model = models.Box
        fields = ["url", "id", "label", "sequence", "folders"]


class FolderDetailSerializer(serializers.ModelSerializer):
    box = BoxListSerializer()
    bundles = BundleListSerializer(many=True)

    class Meta:
        model = models.Folder
        fields = ["url", "id", "label", "sequence", "box", "bundles"]


class BundleDetailSerializer(serializers.ModelSerializer):
    folder = FolderListSerializer()
    documents = DocumentListSerializer(many=True)

    class Meta:
        model = models.Bundle
        fields = ["url", "id", "label", "sequence", "folder", "documents"]


class DocumentDetailSerializer(serializers.ModelSerializer):
    bundle = BundleListSerializer()
    pages = PageSerializer(many=True)

    class Meta:
        model = models.Document
        fields = [
            "url",
            "id",
            "label",
            "sequence",
            "pdf",
            "bundle",
            "fulltext",
            "pages",
            "n_pages",
        ]

