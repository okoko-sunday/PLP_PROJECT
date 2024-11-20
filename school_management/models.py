from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage(location='media')
departments = (
    ('Science', 'Science'),
    ('Arts', 'Arts'),
    ('Commercial', 'Commercial')
)

classes = (
    ('JSS1', 'JSS1'),('JSS2', 'JSS2'),('JSS3', 'JSS3'),
    ('SS1', 'SS1'),('SS2', 'SS2'),('SS3', 'SS3')
)

class Student(models.Model):
    first_name = models.CharField(max_length=225, null=True, blank=True, verbose_name='First Name')
    middle_name = models.CharField(max_length=225, null=True, blank=True, verbose_name='Middle Name')
    last_name = models.CharField(max_length=225, null=True, blank=True, verbose_name='Last Name')
    age = models.IntegerField(verbose_name='Age')
    profile_photo = models.ImageField(upload_to='media', null=True, storage=fs, verbose_name='Profile Photo')
    father_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Father No.')
    mother_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Mother No.')
    guardian_name = models.CharField(max_length=225, blank=True, null=True, verbose_name='Guardian Name')
    home_address = models.TextField()
    current_class = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True)
    department = models.CharField(max_length=225, choices=departments, blank=True, null=True)
    subject = models.ManyToManyField('Subject', through='Grade')
    
    class Meta:
        db_table = 'STUDENT PROFILE'
        verbose_name = 'STUDENT PROFILE'
        
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
    

class Class(models.Model):
    level = models.CharField(max_length=225, choices=classes)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'CLASS'
        verbose_name = 'CLASS'

    def __str__(self):
        return self.level
    
class Subject(models.Model):
    name = models.CharField(max_length=225)
    class_level = models.ForeignKey(Class, on_delete=models.CASCADE)
    department = models.CharField(max_length=225, choices=departments, blank=True, null=True)
    
    class Meta:
        db_table = 'SUBJECT'
        verbose_name = 'SUBJECT'
    
    def __str__(self):
        return f'{self.class_level} {self.name}'
    
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField()
    date_enrolled = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'GRADE'
        verbose_name = 'GRADE'
        
    def __str__(self):
        return f'{self.student} - {self.subject}: {self.score}'
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_attended = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    attended = models.BooleanField()
    
    class Meta:
        db_table = 'ATTENDANCE'
        verbose_name = 'ATTENDANCE'
        
    def __str__(self):
        return f'{self.student} - {self.class_attended} - {self.date}: {'Present' if self.attended else 'Absent'}'
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    
    class Meta:
        db_table = 'TEACHER'
        verbose_name = 'TEACHER'
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject }"
    
# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"{self.student} enrolled in {self.subject }"
    
 