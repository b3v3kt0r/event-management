from rest_framework import viewsets

from events.models import Event
from events.serializers import EventSerializer, EventListSerializer, EventDetailSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return EventListSerializer
        elif self.action == "retrieve":
            return EventDetailSerializer
        return EventSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return self.queryset.select_related()
        return queryset
