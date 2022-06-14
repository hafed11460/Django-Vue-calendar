from django.contrib import admin

from source.models import Source, Event

class SourceAdmin(admin.ModelAdmin):
    list_display = ('id','user','name', )

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','source', 'date', 'color', )
# Register your models here.
admin.site.register(Source,SourceAdmin)
admin.site.register(Event, EventAdmin)