from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('create/', views.create_quiz, name='create_quiz'),
    path('join/<str:code>/', views.join_quiz, name='join_quiz'),
    path('result/<int:quiz_id>/', views.quiz_result, name='quiz_result'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('view/<int:quiz_id>/', views.quiz_view, name='quiz_view'),
    # path('quiz/<int:quiz_id>/results/', views.view_quiz_results, name='view_quiz_results'),
    path('join_room/' , views.join_room , name="join_room") ,
    path('quiz/delete/<int:pk>/', views.delete_quiz, name='delete_quiz'),
] 