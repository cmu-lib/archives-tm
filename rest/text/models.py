from django.db import models
from physical.models import Document, uuidModel
from django.contrib.postgres.fields import ArrayField


class UserCreatedModel(uuidModel):
    pass


class DocumentCollection(UserCreatedModel):
    documents = models.ManyToManyField(Document, related_name="document_collections")


class TopicModel(UserCreatedModel):
    document_collection = models.ForeignKey(
        DocumentCollection, on_delete=models.CASCADE, related_name="topic_models"
    )
    n_topics = models.PositiveIntegerField()
    created_model = models.BinaryField(null=True, blank=True)

    def run(self):
        text_tokens = document_collection.documents.all().values_list(
            "fulltext", flat=True
        )

    @property
    def is_calculated(self):
        return created_model is None


class Topic(uuidModel):
    topic_model = models.ForeignKey(
        TopicModel, on_delete=models.CASCADE, related_name="topics"
    )
    terms = ArrayField(models.CharField(max_length=100))
    documents = models.ManyToManyField(
        Document, through="DocumentTopic", through_fields=("topic", "document")
    )


class DocumentTopic(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    log = models.FloatField(db_index=True)
