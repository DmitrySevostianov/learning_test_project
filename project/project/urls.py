from django.contrib import admin

from django.urls import path, re_path , include
from django.conf import settings
#from django.conf.urls import include

from django.views.generic.base import TemplateView




urlpatterns = [
	path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('learning/', include('learning.urls')),
    path('conspectus/', include('conspectus.urls')),
    
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns