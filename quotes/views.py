from django.shortcuts import render
from django.views.generic import ListView

from quotes.models import Quote


class QuoteListView(ListView):
    template_name = "quotes/index.html"
    paginate_by = 10
    queryset = Quote.with_relations.all()
