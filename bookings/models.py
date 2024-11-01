from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from events.models import Event


class Booking(models.Model):
    class TicketType(models.TextChoices):
        REGULAR = "Regular", _("Regular")
        VIP = "VIP", _("VIP")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bookings")
    ticket_type = models.CharField(max_length=10, choices=TicketType.choices, verbose_name=_("Ticket Type"))
    quantity = models.PositiveIntegerField(verbose_name=_("Ticket Quantity"))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Price"))

    booked_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Booked At"))
