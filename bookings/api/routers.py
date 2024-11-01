from project.router import router
from bookings.api.views import BookingViewSet

router.register("bookings", BookingViewSet, basename="booking")
