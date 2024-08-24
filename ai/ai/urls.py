from django.urls import path
from .views import *

urlpatterns = [
    # path('create/' , create_quiz , name="ai_create")
    path('quiz/' , quiz_view , name="ai_quiz"),
    path('ai_select/' , ai_select , name="ai_select")
]