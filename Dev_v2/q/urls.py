from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_quiz, name='create_quiz'),
    path('join/<str:code>/', views.join_quiz, name='join_quiz'),
    path('result/<int:quiz_id>/', views.quiz_result, name='quiz_result'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/results/', views.view_quiz_results, name='view_quiz_results'),
    path('join_room/' , views.join_room , name="join_room") ,
]