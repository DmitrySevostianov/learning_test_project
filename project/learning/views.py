from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from django.views.generic import TemplateView, ListView, DetailView


from .models import Course, Lesson

class AboutView(TemplateView):
    template_name = "learning/about.html"


class CourseList(ListView):
    model = Course
    course_id = Course.pk
    ##contest_object_name = 'my_courses'  ???


class CourseDetail(DetailView):
    model = Course
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        self.course = get_object_or_404(Course, slug = self.kwargs['slug'])    
        
        context['lessons_list'] = Lesson.objects.filter(course=self.course)
        
        return context
    
    queryset = Course.objects.all()
    


class LessonDetail(DetailView):
    model = Lesson

    
