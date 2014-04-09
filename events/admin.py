from django.contrib import admin
from events.models import Event, Category, Assistant


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'publisher', 'confirmed')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class AssistantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'confirmed')
    readonly_fields = ('user', 'event', 'confirmed')

admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Assistant, AssistantAdmin)