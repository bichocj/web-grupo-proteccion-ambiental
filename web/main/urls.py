from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.render_home),
    url(r'^(?P<page_slug>[\w\.-]+)/$', views.render_page),
]