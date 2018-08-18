from django.urls import path

from . import views

app_name = 'conspectus'

urlpatterns = [
    
    path('about/', views.AboutView.as_view(), name='about'),

]