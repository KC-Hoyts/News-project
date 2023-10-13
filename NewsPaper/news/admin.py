from django.contrib import admin
from .models import Category, Post, Comment, PostCategory, Author
from modeltranslation.admin import TranslationAdmin # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)


class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post


class CommentAdmin(TranslationAdmin):
    model = Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ("author", "categoryType", "date_creation", "title", "text"[0:15],"rating")
    list_filter = ("date_creation", "rating")
    search_fields = ["categoryType"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment, CommentAdmin)