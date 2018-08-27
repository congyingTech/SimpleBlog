# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create your models here.

# 暂时有两个model，用来存储文章的信息和文章的评论


class Post(models.Model):
    title = models.CharField(max_length=256)  # 用于存储文章名字
    view_count = models.IntegerField(default=0)  # 用于存储文章浏览次数
    author = models.CharField(max_length=20)  # 用于存储文章的作者
    content = models.TextField()  # 用于存储文章的内容
    pub_date = models.DateTimeField(default=datetime.now, blank=True)  # 用于存储文章发布时间

    category = models.CharField(max_length=10)  # 预留，为以后文章分类

    def __str__(self):
        content = dict()
        content['title'] = self.title
        content['views'] = self.view_count
        content['author'] = self.author
        return str(content)

    def increase_view(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])


class Comment(models.Model):
    text = models.CharField(max_length=200)  # 评论内容
    nick_name = models.CharField(max_length=10)   # 评论作者
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 关联外键
    count = models.IntegerField(default=0)  # 评论的条数
    pub_date = models.DateTimeField(default=datetime.now, blank=True)  # 用于存储评论发布时间

    def __str__(self):
        content = dict()
        content['text'] = self.text
        content['count'] = self.count
        content['nick_name'] = self.nick_name
        return str(content)


class Tag(models.Model):
    tag_name = models.CharField(max_length=64)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name


