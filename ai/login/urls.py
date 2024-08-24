from django.urls import path
from .views import *
# from . import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('student/signup/', student_signup, name='student_signup'),
    path('teacher/signup/', teacher_signup, name='teacher_signup'),
    path('login/', login_view, name='login'),
    path('student/home/', home_std , name='student_home'),
    path('teacher/home/', home_tea , name='teacher_home'),
    path('logout/', logout_view , name='logout'),
    path('' , root , name="landing"),
]
