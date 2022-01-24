from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'intro',
        'body_one',
        'body_two',
        'author',
        'published_date',
    )


admin.site.register(Blog, BlogAdmin)