from django.contrib import admin
from .models import Category, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'created_date', 'published_date']

admin.site.register(Post)
admin.site.register(Category)
