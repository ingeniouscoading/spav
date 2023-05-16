from django.contrib import admin
from .models import Noticeboard

# Register your models here.

@admin.register(Noticeboard)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('notice_title', 'notice_attachment', 'notice_link', 'notice_created_at')
    list_filter = ('notice_uploaded_by', 'notice_created_at')
    search_fields = ('notice_title', 'notice_created_at')