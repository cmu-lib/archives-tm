from django.db import models
from physical.models import Document, uuidModel
from django.contrib.postgres.fields import ArrayField
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from gensim.models import Phrases, LdaModel
from gensim.corpora import Dictionary
from gensim.test.utils import datapath


class UserCreatedModel(uuidModel):
    pass


class TopicModel(UserCreatedModel):
    MODEL_PATH = "/vol/models"
    documents = models.ManyToManyField(Document, related_name="topic_models")
    n_topics = models.PositiveIntegerField()
    created_model = models.FilePathField(path=MODEL_PATH, null=True)
    document_ids = ArrayField(models.UUIDField())

    def run(self, overwrite=False):
        if self.is_calculated and overwrite is False:
            print(
                f"{self} has already saved a model at {self.created_model}. Run with `overwrite=True` to revise the model"
            )
            return None

        # Wipe any topics formerly associated with this tm
        Topic.objects.filter(topic_model=self).delete()

        docs = list(self.documents.all().values_list("fulltext", flat=True))

        # Captured ordered document IDs when generating the model
        doc_ids = list(self.documents.all().values_list("id", flat=True))
        self.document_ids = doc_ids
        self.save()

        # Split the documents into tokens.
        tokenizer = RegexpTokenizer(r"\w+")
        for idx in range(len(docs)):
            docs[idx] = docs[idx].lower()  # Convert to lowercase.
            docs[idx] = tokenizer.tokenize(docs[idx])  # Split into words.

        # Remove numbers, but not words that contain numbers.
        docs = [[token for token in doc if not token.isnumeric()] for doc in docs]

        # Remove words that are only one character.
        docs = [[token for token in doc if len(token) > 1] for doc in docs]

        # Remove stopwords
        english_stops = set(stopwords.words("english"))
        docs = [[token for token in doc if not token in english_stops] for doc in docs]

        # Lemmatize the documents.

        lemmatizer = WordNetLemmatizer()
        docs = [[lemmatizer.lemmatize(token) for token in doc] for doc in docs]

        #  Compute bigrams.

        # Add bigrams and trigrams to docs (only ones that appear 20 times or more).
        bigram = Phrases(docs, min_count=20)
        for idx in range(len(docs)):
            for token in bigram[docs[idx]]:
                if "_" in token:
                    # Token is a bigram, add to document.
                    docs[idx].append(token)

        # Create a dictionary representation of the documents.
        dictionary = Dictionary(docs)

        # Filter out words that occur less than 20 documents, or more than 50% of the documents.
        dictionary.filter_extremes(no_below=20, no_above=0.5)

        # Bag-of-words representation of the documents.
        corpus = [dictionary.doc2bow(doc) for doc in docs]

        # Set training parameters.
        num_topics = 10
        chunksize = 2000
        passes = 20
        iterations = 400
        eval_every = None  # Don't evaluate model perplexity, takes too much time.

        # Make a index to word dictionary.
        temp = dictionary[0]  # This is only to "load" the dictionary.
        id2word = dictionary.id2token

        model = LdaModel(
            corpus=corpus,
            id2word=id2word,
            chunksize=chunksize,
            alpha="auto",
            eta="auto",
            iterations=iterations,
            num_topics=num_topics,
            passes=passes,
            eval_every=eval_every,
        )
        instance_path = f"{self.MODEL_PATH}/{self.id}.mm"
        model.save(instance_path)
        self.created_model = instance_path
        self.save()

        predictions = [model[doc] for doc in corpus]

        topic_objects = []
        for i, t in enumerate(model.top_topics(corpus)):
            terms = [term[1] for term in t[0]]
            topic_objects.append(
                Topic.objects.create(topic_model=self, terms=terms, index=i)
            )

        for i, pred in enumerate(predictions):
            for ti, t in enumerate(pred):
                DocumentTopic.objects.create(
                    document=Document.objects.get(id=doc_ids[i]),
                    topic=topic_objects[ti],
                    log=t[1],
                )

    @property
    def is_calculated(self):
        return self.created_model is None


class Topic(uuidModel):
    topic_model = models.ForeignKey(
        TopicModel, on_delete=models.CASCADE, related_name="topics"
    )
    terms = ArrayField(models.CharField(max_length=100))
    index = models.PositiveIntegerField()
    documents = models.ManyToManyField(
        Document, through="DocumentTopic", through_fields=("topic", "document")
    )

    class Meta:
        ordering = ["topic_model", "index"]
        unique_together = ("topic_model", "index")


class DocumentTopic(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    log = models.FloatField(db_index=True)
