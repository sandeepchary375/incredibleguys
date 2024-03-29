from blog.models import Post
from django import template
from django.db.models import Count
from django.conf import settings
register = template.Library()


@register.simple_tag
def total_posts():
    return Post.objects.count()


@register.inclusion_tag('blog/latest_post123.html')
def show_latest_posts():
    latest_posts = Post.objects.order_by('-publish')[ :3]
    return{'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]