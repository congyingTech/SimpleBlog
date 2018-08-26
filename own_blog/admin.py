# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Comment


# Register your models here.


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'author']}),

        ('Post Content', {'fields': ['content'], 'classes': ['collapse']}),
        ('Pub Date', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]

    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
