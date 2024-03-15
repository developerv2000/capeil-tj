from typing import Iterable
from django.db import models
from django.utils.text import slugify

from mainapp.models import SluggableByNameModel


class WithQuotesManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().prefetch_related('quote_set', 'quote_set__author', 'quote_set__categories')


class Category(SluggableByNameModel):
    name = models.CharField(max_length=255, unique=True)
    objects = models.Manager()
    with_quotes = WithQuotesManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
