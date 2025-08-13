from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student


class StudentInline(admin.StackedInline):
    model = Student

class CustomUserAdmin(UserAdmin):
    inlines = [
        StudentInline,
    ]
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("role",)}),
    )
    list_display = ("username", "email", "role", "is_superuser", "is_staff")

admin.site.register(User, CustomUserAdmin)