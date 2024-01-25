from django.contrib import admin
from .models import Post, Comments

# Регистрация модели Post в админке
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

# Регистрация модели Comments в админке
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')