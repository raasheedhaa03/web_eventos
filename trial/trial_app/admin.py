from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile

@admin.register(User)
class User(BaseUserAdmin):
    add_fieldsets=(
    (None,{
    'classes':('wide',),
    'fields':('username','password1','password2','email','reg_no','dept','ph_no')
    })
    )
