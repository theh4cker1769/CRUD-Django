from django.contrib import admin
from .models import User, Item

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone', 'profileImg')

admin.site.register(Item)
