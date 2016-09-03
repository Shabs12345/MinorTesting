from django.contrib import admin
from .models import Users


# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    readonly_fields = ["comp_id"]


admin.site.register(Users, UsersAdmin)
