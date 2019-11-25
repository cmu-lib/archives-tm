from django.db import models
from physical.models import Document, uuidModel


class Collection(uuidModel):
    label = models.TextField(unique=True)
    description = models.TextField(blank=True, max_length=10000)


class Series(uuidModel):
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name="seriess"
    )


class DocumentRecord(uuidModel):
    document = models.OneToOneField(
        Document, on_delete=models.CASCADE, related_name="record"
    )
    document_format = models.ForeignKey(
        "DocumentFormat", on_delete=models.CASCADE, related_name="records", null=True
    )
    document_subject = models.ForeignKey(
        "DocumentSubject", on_delete=models.CASCADE, related_name="records", null=True
    )
    created_date_text = models.CharField(blank=True, null=False, max_length=1000)
    coverage_text = models.CharField(blank=True, null=False, max_length=1000)
    document_subject_text = models.CharField(blank=True, null=False, max_length=1000)


class DocumentFormat(uuidModel):
    pass


class DocumentSubject(uuidModel):
    pass
