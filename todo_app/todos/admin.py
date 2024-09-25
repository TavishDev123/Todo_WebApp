from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

# You can customize the UserAdmin settings
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

# Register the UserAdmin with the default User model
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


