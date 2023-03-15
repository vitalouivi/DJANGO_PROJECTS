from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('slug', 'email', 'telephone', 'registered')
    list_display_links = ('slug', 'email', 'telephone', 'registered')
    search_fields = ('slug', 'email', 'telephone', 'registered')
    #prepopulated_fields = {"username": ("username",)}


admin.site.register(User, UserAdmin)
# Register your models here.
