from django.contrib import admin

from .models import Post, Task



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')

