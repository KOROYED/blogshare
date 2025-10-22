from django.contrib import admin
from .models import Category, Post, Comment
from django.contrib.auth.models import User

#admin.site.register(Post)
#admin.site.register(Author)
admin.site.register(Category)
#admin.site.register(Comment)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')


@admin.register(Post)                                           # Register the Admin classes for Post using the decorator     
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_category')
    list_filter = ('created_on', 'last_modified')

    #fields = ['title']                                           Controlling which fields are displayed and laid out


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'display_body')
    list_filter = ('created_on', 'last_modified')