from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path(
        "shorten_url",
        views.ShortenURLView.as_view(),
        name="shorten_urls",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
