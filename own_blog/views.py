# -*- coding: utf-8 -*-
from __future__ import unicode_literals
''
from django.shortcuts import render

from django.views import generic

from .models import Post, Comment

import markdown

from django.shortcuts import get_object_or_404

from django.http import Http404

from django.urls import reverse

# Create your views here.


class HomePageView(generic.ListView):
    template_name = 'own_blog/home_page.html'
    context_object_name = 'all_post_list'

    def get_queryset(self):  # TODO:未来改成分页的形式
        return Post.objects.order_by('-pub_date')  # 按照pub的时间倒叙排列


# class DetailView(generic.DeleteView):
#     model = Post
#     template_name = 'own_blog/post_detail.html'

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.increase_view()  # 跳转到detail的时候就进行increase
    post.content = markdown.markdown(post.content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    context = {'post': post}
    return render(request, 'own_blog/post_detail.html', context=context)


def archives(request):
    try:
        post_list = Post.objects.order_by('-pub_date')
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {"post_list": post_list, "error": False})





# def view_page(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     try:
#         view_post = post.view_count.get(pk=request.POST['post'])
#     except KeyError:
#         return render(request, 'own_blog/home_page.html', {
#             "post": post,
#             "err_msg": "You don't view a post."
#         })
#     else:
#         view_post.view_count += 1  # 执行动作view page的时候把view count进行加1
#         view_post.save()  # 保存到数据库
#         return HttpResponseRedirect(reverse('own_blog:post_detail', args=(post.id,)))


