from rest_framework import serializers
from .models import Message


class MessageDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text', 'status', 'created_at']

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError('text must not be empty')
        return value