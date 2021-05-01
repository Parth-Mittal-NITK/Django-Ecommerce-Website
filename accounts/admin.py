from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from accounts.models import Address

class AddressInLine(admin.StackedInline):
    model = Address
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (AddressInLine,)
# Register your models here.

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


