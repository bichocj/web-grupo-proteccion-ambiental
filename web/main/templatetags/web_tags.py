from django import template
from main.models import Post
register = template.Library()

@register.simple_tag
def get_posts():
	return Post.objects.all()