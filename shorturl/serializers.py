from rest_framework import serializers


class CreateShortURLInputSerializer(serializers.Serializer):
    original_url = serializers.URLField(
        required=True,
        min_length=1,
        max_length=2048,
        error_messages={
            "required": "The original_url shouldn't be null.",
            "max_length": "The original_url is too long.",
        },
    )
