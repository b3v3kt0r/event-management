from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from events.filters import EventFilter
from events.models import Event
from events.serializers import (
    EventSerializer,
    EventListSerializer,
    EventDetailSerializer
)
from events.utils import send_event_registration_email


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter

    def get_serializer_class(self):
        if self.action == "list":
            return EventListSerializer
        elif self.action == "retrieve":
            return EventDetailSerializer
        return EventSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            return self.queryset.prefetch_related("participants")
        return queryset

    @extend_schema(
        description="Join an event as a participant.",
        methods=["POST"],
        request=None,
        responses={
            status.HTTP_200_OK: OpenApiParameter(
                "detail",
                description="Successfully joined the event.",
                type=str
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiParameter(
                "detail",
                description="You are already a participant of this event.",
                type=str
            ),
        },
    )
    @action(
        detail=True,
        methods=["post"],
        url_path="join",
        url_name="join_event",
        permission_classes=[permissions.IsAuthenticated]
    )
    def join_event(self, request, pk=None):
        event = self.get_object()
        user = request.user

        if event.participants.filter(id=user.id).exists():
            return Response(
                {"detail": "You are already a participant of this event."},
                status=status.HTTP_400_BAD_REQUEST
            )

        event.participants.add(user)
        event.save()

        send_event_registration_email(user, event)

        return Response(
            {"detail": "You have joined the event successfully."},
            status=status.HTTP_200_OK
        )

    @extend_schema(
        description="Leave an event as a participant.",
        methods=["DELETE"],
        request=None,
        responses={
            status.HTTP_200_OK: OpenApiParameter(
                "detail",
                description="Successfully left the event.",
                type=str
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiParameter(
                "detail",
                description="You are not a participant of this event.",
                type=str
            ),
        },
    )
    @action(
        detail=True,
        methods=["delete"],
        url_path="leave",
        url_name="leave_event",
        permission_classes=[permissions.IsAuthenticated]
    )
    def leave_event(self, request, pk=None):
        event = self.get_object()
        user = request.user

        if not event.participants.filter(id=user.id).exists():
            return Response(
                {"detail": "You are not a participant of this event."},
                status=status.HTTP_400_BAD_REQUEST
            )

        event.participants.remove(user)
        event.save()

        return Response(
            {"detail": "You have left the event successfully."},
            status=status.HTTP_200_OK
        )
