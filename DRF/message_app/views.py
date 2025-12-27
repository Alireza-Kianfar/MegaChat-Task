from rest_framework import viewsets, filters

try:
    from django_filters.rest_framework import DjangoFilterBackend
    FILTER_BACKENDS = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
except Exception:
    FILTER_BACKENDS = [filters.OrderingFilter, filters.SearchFilter]

from .models import Message
from .serializers import MessageDataSerializer


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('-created_at')
    serializer_class = MessageDataSerializer
    pagination_class = None
    filter_backends = FILTER_BACKENDS
    filterset_fields = ['status']
    ordering_fields = ['created_at']
    search_fields = ['text']