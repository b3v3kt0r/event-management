from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

from events.models import Event


class EventModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")

        self.event = Event.objects.create(
            title="Test Event",
            description="This is a test description.",
            date=timezone.now(),
            location="Test Location",
            organizer="Test Organizer"
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, "Test Event")
        self.assertEqual(self.event.description, "This is a test description.")
        self.assertEqual(self.event.location, "Test Location")
        self.assertEqual(self.event.organizer, "Test Organizer")
        self.assertIsInstance(self.event.date, timezone.datetime)

    def test_event_str_method(self):
        self.assertEqual(str(self.event), "Test Event")

    def test_add_participant(self):
        self.event.participants.add(self.user)
        self.assertIn(self.user, self.event.participants.all())

    def test_remove_participant(self):
        self.event.participants.add(self.user)
        self.event.participants.remove(self.user)
        self.assertNotIn(self.user, self.event.participants.all())

    def test_event_with_multiple_participants(self):
        user2 = get_user_model().objects.create_user(username="testuser2", password="testpass2")
        self.event.participants.add(self.user, user2)
        self.assertIn(self.user, self.event.participants.all())
        self.assertIn(user2, self.event.participants.all())
        self.assertEqual(self.event.participants.count(), 2)
