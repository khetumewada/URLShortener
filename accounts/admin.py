from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Contact

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # fields shown in list view
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_active")
    # fields you can filter by
    list_filter = ("is_staff", "is_superuser", "is_active")
    # search bar fields
    search_fields = ("username", "email")
    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_staff", "is_active")}
        ),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Fields shown in list view
    list_display = ("id", "title", "subject", "email", "timestamp")
    # Fields available for search
    search_fields = ("title", "subject", "email", "message")
    # Filters in sidebar
    list_filter = ("timestamp",)
    # Order: newest first
    ordering = ("-timestamp",)
    readonly_fields = ("timestamp",)
