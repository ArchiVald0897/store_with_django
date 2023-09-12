from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'text', 'blog_img', 'date_of_creation', 'is_published', 'count_of_views')
