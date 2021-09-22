from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'content']
    list_display = ['author', 'content', 'created']
