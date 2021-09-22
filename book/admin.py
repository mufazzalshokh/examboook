from django.contrib import admin

from book.models import BookModel, AuthorModel, UserModel, CategoryModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'page_count', 'author']
    search_fields = ['title', 'author']
    list_filter = ['created_at']


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_filter = ['created_at', 'updated_at']
