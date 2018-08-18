from django.urls import path

from . import views

app_name = 'learning'

urlpatterns = [
    
    path('about/', views.AboutView.as_view(), name='about'),

    path('courses', views.CourseList.as_view(), name='courses_list'),
    
    path('courses/<int:pk>', views.LessonDetail.as_view(), name='lesson_detail'),
    
    path('courses/<slug:slug>', views.CourseDetail.as_view(), name='course_detail'),
    

]