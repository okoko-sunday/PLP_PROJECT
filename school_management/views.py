from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    return render(request, 'base.html')

def student(request):
    students = models.Student.objects.all()
    context = {'students': student}
    return render(request, 'student/profile.html', context)