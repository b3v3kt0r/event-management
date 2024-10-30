import os

from django.core.mail import send_mail
from dotenv import load_dotenv

load_dotenv()


def send_event_registration_email(user, event):
    subject = f"Registration for the {event.title} event is successful."

    event_date_formatted = event.date.strftime("%d %B %Y %H:%M")

    message = (
        f"Hello, {user.username}!\n\n"
        f"We are waiting for you on {event_date_formatted}.\n\n"
        "Thanks for your interest!"
    )
    recipient_list = [user.email]

    email_from = os.environ.get("EMAIL_HOST_USER")

    send_mail(subject, message, email_from, recipient_list)
