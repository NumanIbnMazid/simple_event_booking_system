from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Event Name"))
    date = models.DateField(verbose_name=_("Event Date"))
    location = models.CharField(max_length=255, verbose_name=_("Location"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))

    # Ticket information
    total_regular_tickets = models.PositiveIntegerField(verbose_name=_("Total Regular Tickets"))
    total_vip_tickets = models.PositiveIntegerField(verbose_name=_("Total VIP Tickets"))
    available_regular_tickets = models.PositiveIntegerField(verbose_name=_("Available Regular Tickets"))
    available_vip_tickets = models.PositiveIntegerField(verbose_name=_("Available VIP Tickets"))

    # Pricing
    regular_ticket_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("Regular Ticket Price"))
    vip_ticket_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("VIP Ticket Price"))

    # Early bird details
    early_bird_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("Early Bird Price"))
    early_bird_deadline = models.DateTimeField(verbose_name=_("Early Bird Deadline"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def is_early_bird(self):
        """Check if the current date is within the early bird period."""
        return timezone.now() <= self.early_bird_deadline

    def __str__(self):
        return self.name
