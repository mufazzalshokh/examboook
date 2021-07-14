from django.contrib import admin

from book.models import BookModel


@admin.register(BookModel)
class BooksModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'author']
