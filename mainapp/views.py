from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "pages/home.html"
    http_method_names = ("head", "get")
