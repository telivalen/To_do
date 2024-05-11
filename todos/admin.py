from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ('title', 'body')
    list_filter = ('title', 'body')
    list_per_page = 10
    ordering = ('title',)

admin.site.register(Task, TaskAdmin)