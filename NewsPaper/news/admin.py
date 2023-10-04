from django.contrib import admin
from .models import Category, Author, Post, PostCategory, Comment

class NewsAdmin(admin.ModelAdmin):
    list_display = ("author", "categoryType", "date_creation", "title", "text"[0:15],"rating")
    list_filter = ("date_creation", "rating")
    search_fields = ["categoryType"]


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post, NewsAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)