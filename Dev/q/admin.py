# from django.contrib import admin
# from .models import Quiz, Question, QuizResult

# admin.site.register(Quiz)
# admin.site.register(Question)
# admin.site.register(QuizResult)

from django.contrib import admin
from .models import Quiz, Question, QuizResult

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Number of empty forms for new questions in the admin

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'host', 'created_at')
    search_fields = ('title', 'code', 'host__username')
    list_filter = ('created_at',)
    inlines = [QuestionInline]

class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'user', 'score', 'submitted_at')
    search_fields = ('quiz__title', 'user__username')
    list_filter = ('quiz', 'submitted_at')

admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizResult, QuizResultAdmin)
