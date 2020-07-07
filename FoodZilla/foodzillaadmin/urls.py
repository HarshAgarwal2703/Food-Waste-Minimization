from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'bayer2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('admin/',  admin.site.urls),
    url('', include('ooglorp.urls')),
    
]
