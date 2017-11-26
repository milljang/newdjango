from django.contrib import admin
from .models import Post,comment,Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content','created_at', 'updated_at']
    list_display_links = ['id', 'title']
#    list_editable = ['author']
#    list_per_page = 3
#    list_filter = ['author', 'created_at']


@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display =['name']