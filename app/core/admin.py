from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#recommended convention for converting strings in python to human readable text
from django.utils.translation import gettext as _

from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    #define the sections for the field sets in the change and create page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal Info'), {'fields': ('name',)}),
        (
            ('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),#make sure to include the comma at the end because we only have 1 item in the list and we don't want python to think it's an object
    )

admin.site.register(models.User, UserAdmin)
