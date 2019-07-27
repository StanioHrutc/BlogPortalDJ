from django.contrib import admin

# Register your models here.

from .models import Work


class WorkAdmin(admin.ModelAdmin):

    list_display       = ('title', 'creation_date')
    list_display_links = ('title', 'creation_date')
    search_fields      = ('title', 'creation_date')
    list_per_page      = 15


admin.site.register(Work, WorkAdmin,)