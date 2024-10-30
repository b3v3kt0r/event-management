from rest_framework import serializers

from events.models import Event
from user.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    number_of_participants = serializers.IntegerField(
        source="participants.count",
        read_only=True
    )

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "date",
            "location",
            "organizer",
            "number_of_participants",
            "participants"
        ]


class EventListSerializer(EventSerializer):
    participants = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="username")


class EventDetailSerializer(EventSerializer):
    participants = UserSerializer(many=True, read_only=True)
