from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
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

    def save(self, *args, **kwargs):
        """Override save to calculate total price based on ticket type and apply early bird discount if applicable."""
        if not self.pk:  # Only calculate the total price for new bookings
            if self.ticket_type == self.TicketType.VIP:
                ticket_price = self.event.vip_ticket_price
            else:
                ticket_price = (
                    self.event.early_bird_price if self.event.is_early_bird() else self.event.regular_ticket_price
                )
            self.total_price = ticket_price * self.quantity

            # Reduce available tickets in the event
            if self.ticket_type == self.TicketType.VIP:
                if self.quantity > self.event.available_vip_tickets:
                    raise ValueError("Not enough VIP tickets available.")
                self.event.available_vip_tickets -= self.quantity
            else:
                if self.quantity > self.event.available_regular_tickets:
                    raise ValueError("Not enough regular tickets available.")
                self.event.available_regular_tickets -= self.quantity
            self.event.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.event} - {self.ticket_type}"
