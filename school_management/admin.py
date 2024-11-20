from django.contrib import admin
from .models import Student, Subject, Class, Teacher, Attendance, Grade

# Register your models here.
class GradeInline(admin.TabularInline):
    model = Grade
    extra = 1
    
class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 1
    # fields = []


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'profile_photo']
    inlines = [GradeInline, AttendanceInline]
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'class_level', 'department')
    
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    # inlines = [StudentInline]
    pass

    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'subject', 'email')
    
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_filter = ['student', 'subject']