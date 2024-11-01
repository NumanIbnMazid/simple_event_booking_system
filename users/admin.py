from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                    "is_vip",
                    "password",
                    "date_joined",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )

    list_display = (
        "id",
        "email",
        "username",
        "is_vip",
        "is_staff",
        "is_superuser",
        "date_joined",
    )
    list_filter = ("is_vip", "is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("email", "username")
    readonly_fields = (
        "date_joined",
    )
    ordering = ("-date_joined",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


admin.site.register(get_user_model(), UserAdmin)
