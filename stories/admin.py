from django.contrib import admin

# Register your models here.
from stories.models import Story


# customise displaying the model
class StoryAdmin(admin.ModelAdmin):

    list_display       = ('id', 'title', 'publication_date', 'is_published')
    list_display_links = ('title', 'publication_date')
    list_filter        = ('publication_date',)
    list_editable      = ('is_published',)
    search_fields      = ('title', 'publication_date', 'is_published')
    list_per_page      = 20


admin.site.register(Story, StoryAdmin,)