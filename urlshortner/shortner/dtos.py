from rest_framework import serializers


class ValidateShortenURLParams(serializers.Serializer):
    url = serializers.URLField()


class ValidateShortenURLID(serializers.Serializer):
    shorten_path = serializers.CharField(max_length=10000)
