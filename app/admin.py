from django.contrib import admin
from .models import Entries

class EntriesAdmin(admin.ModelAdmin):
    list_display=('host_name','visitor_name')
    list_display_links=(['host_name','visitor_name'])
    search_fields=('host_name','visitor_name,')
    list_per_page=25

admin.site.register(Entries,EntriesAdmin)
# Register your models here.
