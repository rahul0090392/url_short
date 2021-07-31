from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path(
        "manageurl/shorten_url",
        views.ShortenURLView.as_view(),
        name="shorten_urls",
    ),
    path(
        "manageurl/shorten_url/<str:shorten_path>",
        views.ShortenURLResolveView.as_view(),
        name="shorten_url_resolve",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
