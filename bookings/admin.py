from django.contrib import admin
from utils.snippets import CustomModelAdminMixin
from bookings.models import Booking


# ----------------------------------------------------
# *** Booking ***
# ----------------------------------------------------

class BookingAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    class Meta:
        model = Booking


admin.site.register(Booking, BookingAdmin)
