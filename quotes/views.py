from django.shortcuts import render
from django.views.generic import ListView

from quotes.models import Quote


class QuoteListView(ListView):
    model = Quote
    template_name = "quotes/index.html"


