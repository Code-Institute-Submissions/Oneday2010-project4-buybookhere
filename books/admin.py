from django.contrib import admin
from .models import Book, Category

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'title',
        'author',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('code',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_title',
        'title',
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
