from django.contrib import admin

from .models import Project, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'technologies',
        'created_at',
    )

    search_fields = (
        'title',
        'technologies',
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
    )