from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index),
    url(r'^homepage$',views.index),
    url(r'^aboutus$',views.aboutus),
    url(r'^admin/', admin.site.urls),

]
