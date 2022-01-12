from django.contrib import admin

# Register your models here.
from myapp.models import UserType

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_verified')
    pass

admin.site.register(UserType, UserTypeAdmin)