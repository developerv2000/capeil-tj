from typing import Any
from django.db.models import QuerySet
from django.db.models.base import Model as Model
from django.shortcuts import render
from django.views.generic import DetailView

from categories.models import Category
from quotes.models import Quote


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = "category"
    template_name = "categories/detail.html"
    queryset = Category.with_quotes
