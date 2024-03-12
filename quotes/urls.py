from django.urls import path
from quotes.views import QuoteListView

app_name = "quotes"
urlpatterns = [
    path("", QuoteListView.as_view(), name="index")
]

