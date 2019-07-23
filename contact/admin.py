from django.contrib import admin

# Register your models here.
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):

    list_display       = ('id', 'name', 'sur_name', 'email', 'is_subscribed')
    list_display_links = ('name', 'sur_name')
    list_editable      = ('is_subscribed',)
    search_fields      = ('id', 'name', 'sur_name', 'is_subscribed')
    list_per_page      = 15


admin.site.register(Contact, ContactAdmin,)
