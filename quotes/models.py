from django.db import models
from mainapp.models import RandomizeableModel, TimestampedModel
from authors.models import Author
from categories.models import Category


class PrefetchedRelationsManager(models.Manager):
    """
    Custom manager that overrides the default queryset retrieval behavior to include
    eager loading of related objects.
    """

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().select_related("author").prefetch_related("categories")


class Quote(TimestampedModel, RandomizeableModel):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    body = models.TextField()
    categories = models.ManyToManyField(Category)
    with_related_objects = PrefetchedRelationsManager()

    def __str__(self):
        return self.body
