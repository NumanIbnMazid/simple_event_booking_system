from project.router import router
from events.api.views import EventViewSet

router.register("events", EventViewSet, basename="events")
