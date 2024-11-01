from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from .models import Booking

@shared_task
def send_reminder_email():
    """Send a reminder email to users with events happening in a week."""
    week_from_now = timezone.now() + timedelta(days=7)
    bookings = Booking.objects.filter(event__date=week_from_now.date())

    for booking in bookings:
        subject = f"Reminder: Upcoming Event '{booking.event.name}'"
        message = (
            f"Hello {booking.user.username},\n\n"
            f"This is a reminder that you have an upcoming event, '{booking.event.name}', "
            f"scheduled on {booking.event.date} at {booking.event.location}.\n\n"
            "Looking forward to seeing you there!"
        )
        send_mail(subject, message, "noreply@event_booking.com", [booking.user.email])
