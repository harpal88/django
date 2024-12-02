from rest_framework import serializers
from .models import Comment, Screenshot

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at']


class ScreenshotSerializer(serializers.ModelSerializer):
    def validate_image(self, value):
        # Limit file size to 2 MB
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("File size must be under 2MB.")
        # Restrict file extensions to PNG, JPG, JPEG
        if not value.name.endswith(('.png', '.jpg', '.jpeg')):
            raise serializers.ValidationError("File must be a PNG or JPG.")
        return value

    class Meta:
        model = Screenshot  # Specify the model to serialize
        fields = ['id', 'image', 'uploaded_at']  # Include fields to be serialized
