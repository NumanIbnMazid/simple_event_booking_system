from .router import router
# Users
from users.api.routers import *
# Events
from events.api.routers import *
# Bookings
from bookings.api.routers import *

app_name = "event_booking_backend_api"
urlpatterns = router.urls
