from django.conf.urls import url
from requests import request

from blogposts.views import post
from . import views

urlpatterns = [
    # url(r'^$',views.index, name='index')
    url(r'^(?P<post_id>.+)$', views.post, name='post')
]
