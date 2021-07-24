from rest_framework import serializers


class ValidateShortenURLParams(serializers.Serializer):
    url = serializers.URLField()
