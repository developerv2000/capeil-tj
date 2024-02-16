from django.db import models
from mainapp.models import TimestampedModel
from authors.models import Author
from categories.models import Category


class Quote(TimestampedModel):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    body = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.body
