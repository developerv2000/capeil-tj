from django.urls import path

from categories.views import CategoryDetailView

app_name = "categories"
urlpatterns = [
    path("/<slug:slug>", CategoryDetailView.as_view(), name="detail")
]

