from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'contact_number')

admin.site.register(User, UserAdmin)