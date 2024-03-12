from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from quotes.models import Quote

class HomePage(TemplateView):
    http_method_names = ("head", "get")
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["quote_of_day"] = Quote.get_random_item('with_related_objects')
        return context
