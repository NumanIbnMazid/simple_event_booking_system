from rest_framework import viewsets, permissions
from bookings.models import Booking
from bookings.api.serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    A viewset for creating and retrieving bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Attach the booking to the logged-in user."""
        serializer.save(user=self.request.user)
