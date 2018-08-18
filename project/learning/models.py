from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    name_for_slug = 'slug_for_course'
    slug = models.SlugField(default = name_for_slug)
    
    def __str__(self):
        return str(self.name)
    
    
class Lesson(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank = True)

    def __str__(self):
        return str(self.name)
