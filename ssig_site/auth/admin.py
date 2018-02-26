from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    add_form_template = 'user_add_form.html'
    add_form = forms.ModelForm

    fieldsets = (
        (None, {'fields': ('upi', 'password')}),
        ('Personal info', {'fields': ('email', 'full_name', 'given_name', 'department')}),
        ('Permissions', {'fields': ('is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('upi',),
        }),
    )

    list_display = ('upi', 'email', 'full_name', 'department')
    list_filter = ('is_superuser',)
    ordering = ('upi',)
