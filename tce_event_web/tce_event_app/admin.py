from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


admin.site.site_header='TCE_event_web Admin'
admin.site.index_title='Admin'
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email','first_name')
    inlines = [ProfileInline]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','email']

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
