from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("categories", include('categories.urls')),
]
