from django.contrib import admin
from utils.snippets import CustomModelAdminMixin
from events.models import Event


# ----------------------------------------------------
# *** Event ***
# ----------------------------------------------------

class EventAdmin(CustomModelAdminMixin, admin.ModelAdmin):
    class Meta:
        model = Event


admin.site.register(Event, EventAdmin)
