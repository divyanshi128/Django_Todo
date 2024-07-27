from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "priority", "is_completed")
    list_filter = ("priority", "is_completed")
    search_fields = ("title", "description")
