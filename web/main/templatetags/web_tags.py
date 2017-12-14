from django import template
from main.models import Post, Category

register = template.Library()


@register.simple_tag
def get_posts():
    return Post.objects.all()


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def get_post_by_id(id):
    return Post.objects.get(id=id)

