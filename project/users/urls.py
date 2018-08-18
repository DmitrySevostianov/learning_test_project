from django.urls import path
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [

	path('about/', TemplateView.as_view(template_name='users/about.html'), name='users_about'),
    path('signup/', views.signup, name='signup'),

]