from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password



class CustomUserAdmin(UserAdmin):
    list_display = ('get_full_name', 'username', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'national_number', 'username', 'phone_number', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    def save_model(self, request, obj, form, change):
        if change and 'password' in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)


