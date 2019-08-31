from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    model=Post
    prepopulated_fields = {'slug':('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'body', 'created', 'updated', 'active']
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)