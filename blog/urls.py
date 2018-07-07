from django.conf.urls import include, url
from django.contrib import admin

import blogposts
from blogposts.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogposts/', include('blogposts.urls')),
    url(r'^$', blogposts.views.index)
]
