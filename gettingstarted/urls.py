# from django.conf.urls import include, url
# from django.urls import path
#
# from django.contrib import admin
# admin.autodiscover()
#
# import hello.views
#
# # Examples:
# # url(r'^$', 'gettingstarted.views.home', name='home'),
# # url(r'^blog/', include('blog.urls')),
#
# urlpatterns = [
#     url(r'^$', hello.views.index, name='index'),
#     url(r'^db', hello.views.db, name='db'),
#     path('admin/', admin.site.urls),
# ]
from django.conf.urls import include, url
from django.contrib import admin

import hello.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    # url(r'', include('hello.urls'))

    url(r'^$', hello.views.index),
    url(r'^product$', hello.views.product),
    url(r'^product2$', hello.views.product2),
    url(r'^product3$', hello.views.product3),
    url(r'^product4$', hello.views.product4),
    url(r'^playlist$', hello.views.playlist),
    url(r'^playlist2$', hello.views.playlist2),
    url(r'^homepage$',hello.views.index),
    url(r'^aboutus$',hello.views.aboutus),
    url(r'^admin/', admin.site.urls),
]
