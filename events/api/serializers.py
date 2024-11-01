from rest_framework import serializers
from events.models import Event
from django.utils import timezone

class EventSerializer(serializers.ModelSerializer):
    regular_ticket_price = serializers.DecimalField(max_digits=8, decimal_places=2, coerce_to_string=False)
    vip_ticket_price = serializers.DecimalField(max_digits=8, decimal_places=2, coerce_to_string=False)
    early_bird_price = serializers.DecimalField(max_digits=8, decimal_places=2, coerce_to_string=False)
    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "date",
            "location",
            "description",
            "total_regular_tickets",
            "total_vip_tickets",
            "available_regular_tickets",
            "available_vip_tickets",
            "regular_ticket_price",
            "vip_ticket_price",
            "early_bird_price",
            "early_bird_deadline",
        ]
        read_only_fields = ['id']

    def validate(self, data):
        """Validate the ticket limits and early bird deadline."""
        if data["total_regular_tickets"] < data["available_regular_tickets"]:
            raise serializers.ValidationError("Available regular tickets exceed the total limit.")
        if data["total_vip_tickets"] < data["available_vip_tickets"]:
            raise serializers.ValidationError("Available VIP tickets exceed the total limit.")
        if data["early_bird_deadline"] < timezone.now():
            raise serializers.ValidationError("Early bird deadline must be a future date.")
        return data
