from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    # path('student/<int:id>/', views.student, name='student')
    path('student/', views.student, name='student'),
    path('student<str:class_name>/', views.student_filter, name='student_filter')
]
