from rest_framework import viewsets, permissions
from events.models import Event
from events.api.serializers import EventSerializer
from rest_framework.exceptions import PermissionDenied

class EventViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing events. Only admins can create and modify events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restrict to admin users only

    def perform_create(self, serializer):
        """
        Override to handle custom create logic if needed.
        """
        serializer.save()

    def get_permissions(self):
        # Apply IsAdminUser permission only for the create, update and delete method
        if self.action in ["create", "update", "destroy"]:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
