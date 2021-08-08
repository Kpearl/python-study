from django.contrib import admin
from bookmarks.models import Bookmarks

@admin.register(Bookmarks)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')