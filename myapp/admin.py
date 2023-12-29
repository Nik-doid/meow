# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser
from .forms import RegistrationForm

class CustomUserAdmin(UserAdmin):
    add_form = RegistrationForm  # Use your custom RegistrationForm for user creation
    form = RegistrationForm  # Use your custom RegistrationForm for user change

    list_display = ('username', 'email', 'full_name', 'photo', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('full_name', 'email', 'photo')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'full_name', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('username', 'email', 'full_name')
    ordering = ('username',)

    def full_name(self, obj):
        return obj.get_full_name()

    def photo(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))

    full_name.short_description = 'Full Name'
    photo.short_description = 'Photo'

admin.site.register(CustomUser, CustomUserAdmin)
