from rest_framework import serializers
from bookings.models import Booking
from events.models import Event
from django.utils import timezone

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "user", "event", "ticket_type", "quantity", "total_price", "booked_at"]
        read_only_fields = ["total_price", "booked_at"]

    def validate(self, data):
        """Validate ticket type and availability based on user VIP status and event."""
        user = self.context["request"].user
        event = data.get("event")
        ticket_type = data.get("ticket_type")
        quantity = data.get("quantity")

        if ticket_type == "VIP" and not user.is_vip:
            raise serializers.ValidationError("Only VIP users can book VIP tickets.")
        
        if event.date < timezone.now().date():
            raise serializers.ValidationError("Cannot book tickets for past events.")
        
        available_tickets = (
            event.available_vip_tickets if ticket_type == "VIP" else event.available_regular_tickets
        )
        
        if quantity > available_tickets:
            raise serializers.ValidationError(f"Not enough {ticket_type.lower()} tickets available.")
        
        return data

    def create(self, validated_data):
        """Calculate total price and reduce available tickets."""
        booking = Booking(**validated_data)
        event = booking.event
        
        ticket_price = event.vip_ticket_price if booking.ticket_type == "VIP" else (
            event.early_bird_price if event.is_early_bird() else event.regular_ticket_price
        )
        booking.total_price = ticket_price * booking.quantity

        # Update event's available ticket count
        if booking.ticket_type == "VIP":
            event.available_vip_tickets -= booking.quantity
        else:
            event.available_regular_tickets -= booking.quantity
        event.save()

        booking.save()
        return booking
