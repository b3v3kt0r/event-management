import django_filters
from events.models import Event


class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains"
    )

    class Meta:
        model = Event
        fields = ["title"]
