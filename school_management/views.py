from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    return render(request, 'base.html')

def student(request ):
    # students = models.Student.objects.get(pk=id)
    students = models.Student.objects.all()
    context = {'students': students}
    return render(request, 'student/profile.html', context)

def student_filter(request, class_name):
    students = models.Student.objects.filter(current_class__level = class_name)
    return render(request, 'student/class_filter.html', {'students':students, 'class_name':class_name})