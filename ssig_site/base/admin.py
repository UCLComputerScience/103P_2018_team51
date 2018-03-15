from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Group)
admin.site.register(models.Event)


@admin.register(models.GroupUser)
class GroupUserAdmin(admin.ModelAdmin):
    list_filter = ('group', 'user')
