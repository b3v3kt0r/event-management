from django.core.mail import send_mail


def send_event_registration_email(user, event):
    subject = f"Registration for the {event.title} event is successful."
    message = f"Hello, {user.username}!\n\nWe are waiting for you on {event.date}. \n\nThanks for your interesting!"
    recipient_list = [user.email]

    send_mail(subject, message, "stanislav.v.sudakov@gmail.com", recipient_list)
