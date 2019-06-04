from django.contrib import admin

from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(User, UserAdmin)
