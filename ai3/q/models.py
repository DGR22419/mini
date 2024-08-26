from django.db import models
import uuid
import random
# from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from login.models import *

static_storage = FileSystemStorage(location=settings.BASE_DIR / 'static/questions')

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    # code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    code = models.IntegerField(unique=True, editable=False, null=True, blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        while True:
            code = random.randint(100000, 999999)
            if not Quiz.objects.filter(code=code).exists():
                return code

    # def __str__(self):
    #     return self.title

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=255)
    image_loc = models.CharField(max_length=255, blank=True, null=True)
    images = models.ImageField(upload_to='questions/', null=True, blank=True)


    def __str__(self):
        return self.question_text
    
# class QuestionAI(models.Model):
#     quiz = models.ForeignKey(Quiz, related_name='ai_questions', on_delete=models.CASCADE)
#     question_text = models.TextField()
#     option1 = models.CharField(max_length=255)
#     option2 = models.CharField(max_length=255)
#     option3 = models.CharField(max_length=255)
#     option4 = models.CharField(max_length=255)
#     correct_option = models.CharField(max_length=255)
#     image = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return self.question_text

class QuizResult(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='results', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.score}"
