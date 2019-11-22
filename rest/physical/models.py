from django.db import models
from django.conf import settings
import uuid

"""
Abstract models
"""


class uuidModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(null=True, blank=False, max_length=400)

    class Meta:
        abstract = True


class sequentialModel(uuidModel):
    sequence = models.PositiveIntegerField(db_index=True)

    class Meta:
        abstract = True
        ordering = ["sequence"]

    def __str__(self):
        return f"{self.label} - {self.sequence}"


"""
Materialized models
"""


class Box(sequentialModel):
    pass


class Folder(sequentialModel):
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name="folders")


class Bundle(sequentialModel):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="bundles")


class Document(sequentialModel):
    bundle = models.ForeignKey(
        Bundle, on_delete=models.CASCADE, related_name="documents"
    )
    fulltext = models.TextField(null=False, blank=True, editable=False)


class Page(sequentialModel):
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="document"
    )
    image = models.CharField(null=True, blank=False, max_length=800)

    @property
    def iiif_base(self):
        return settings.IMAGE_BASEURL + self.image

    @property
    def iiif_info(self):
        return f"{self.iiif_base}/info.json"

    @property
    def full_image(self):
        return f"{self.iiif_base}/full/full/0/default.jpg"

    @property
    def thumbnail_image(self):
        return f"{self.iiif_base}/full/500,/0/default.jpg"

    @property
    def image(self):
        return {
            "id": self.iiif_base,
            "info": self.iiif_info,
            "full": self.full_image,
            "thumbnail": self.thumbnail_image,
        }

