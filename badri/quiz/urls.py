from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing_page'),
    path('login/' , views.login_view , name='login_page' ),
    path('signup/' , views.signup_view , name='signup_page'),
    path('home/' , views.home_view , name='home_page'),
    path('logout/' , views.logout_view , name='logout'),
    # path('profile/' , views.profile_view , name='profile'),
    # path('create_quiz/' , views.create_quiz_view , name='create_quiz' ) ,
    # path('submit-quiz/' , views.submit_quiz_view , name='submit-quiz' )
    # path('create/', views.create_quiz, name='create_quiz'),
    # path('join/<str:code>/', views.join_quiz, name='join_quiz'),
    # path('result/<int:quiz_id>/', views.quiz_result, name='quiz_result'),
    # path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    # path('quiz/<int:quiz_id>/results/', views.view_quiz_results, name='view_quiz_results'),
]
