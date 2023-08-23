from django.contrib import admin
from .models import Course, Lesson


@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course_owner',)
    list_editable = ('course_owner',)
    list_display_links = ('title',)


@admin.register(Lesson)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course', 'lesson_owner',)
    list_editable = ('lesson_owner',)
    list_display_links = ('title',)