from django.contrib import admin
from .models import Messages, Groups, Module


@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['title', 'message', 'slug']
    prepopulated_fields = {'slug': ('title', 'message')}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['created']
    search_fields = ['title', 'group_overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
