from django.shortcuts import render , redirect
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.http import JsonResponse , HttpResponseForbidden
import json
from .forms import SignupForm
from django.contrib.auth.models import User
from .models import *

# def signup_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home_page')
        
#         else :
#             if form.has_error('password2'):
#                 password_error = form.errors['password2']
#     else:
#         form = CustomUserCreationForm()
    # return render(request, 'HTML/register.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create the user
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect('home_page')  
    else:
        form = SignupForm()

    return render(request, 'HTML/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect('home_page')
            next_url = request.GET.get('next', 'home_page')
            return redirect(next_url)
    else:
        form = CustomAuthenticationForm()
    return render(request, 'HTML/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landing_page')

@login_required
def home_view(request):
    user = request.user
    quiz = Quiz.objects.filter(host=user)
    result = QuizResult.objects.filter(user=user)
    return render(request, 'dashboard.html', {'quizzes': quiz, 'results': result})
    # return render(request, 'dashboard.html')

@login_required
def profile_view(request):
    return render(request , 'HTML/profile_page.html')

@csrf_exempt
def landing_view(request):
    return render(request, 'HTML/index.html')

# def error_view(request):
#     return render(request , 'error.html')

def error(request, reason=""):
    return render(request, "error.html", {"reason": reason})

##################################################################################################################
#try 

# @login_required
# def create_quiz(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         questions = request.POST.getlist('questions')
#         options = request.POST.getlist('options')
#         correct_options = request.POST.getlist('correct_options')
        
#         quiz = Quiz.objects.create(title=title, host=request.user)
        
#         for i in range(len(questions)):
#             Question.objects.create(
#                 quiz=quiz,
#                 question_text=questions[i],
#                 option1=options[i*4],
#                 option2=options[i*4 + 1],
#                 option3=options[i*4 + 2],
#                 option4=options[i*4 + 3],
#                 correct_option=correct_options[i]
#             )
        
#         return redirect('quiz_detail', quiz_id=quiz.id)

#     return render(request, 'try/create_quiz.html')

##################################################################################################################

# @login_required
# def create_quiz(request):
#     if request.method == 'POST':
#         # Get the quiz title from the form
#         title = request.POST.get('title')
        
#         # Create the Quiz instance
#         quiz = Quiz.objects.create(title=title, host=request.user)
        
#         # Extract questions and their options
#         questions = request.POST.getlist('questions')
#         options = request.POST.getlist('options')
#         correct_options = request.POST.getlist('correct_options')
        
#         # Iterate through the questions and save them
#         option_index = 0
#         for i, question_text in enumerate(questions):
#             question = Question.objects.create(
#                 quiz=quiz,
#                 question_text=question_text,
#                 option1=options[option_index],
#                 option2=options[option_index + 1],
#                 option3=options[option_index + 2],
#                 option4=options[option_index + 3],
#                 correct_option=correct_options[i]
#             )
#             option_index += 4  # Move to the next set of 4 options
        
#         return redirect('quiz_detail')  # Redirect to a success page or another relevant page

#     return render(request, 'try/create_quiz.html')

# ##################################################################################################################


# def join_quiz(request, code):
#     quiz = get_object_or_404(Quiz, code=code)
    
#     if request.method == 'POST':
#         user_answers = request.POST.getlist('answers')
#         score = 0
        
#         # Make sure the length of user answers matches the number of questions
#         questions = quiz.questions.all()
        
#         for i, question in enumerate(questions):
#             try:
#                 if question.correct_option == user_answers[i]:
#                     score += 1
#             except IndexError:
#                 # Handle the case where there are fewer answers than questions
#                 continue
        
#         # Store the quiz result for the user
#         QuizResult.objects.create(quiz=quiz, user=request.user, score=score)
        
#         return redirect('quiz_result', quiz_id=quiz.id)
    
#     return render(request, 'join_quiz.html', {'quiz': quiz})



# def quiz_result(request, quiz_id):
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     results = quiz.results.all()
#     return render(request, 'quiz_result.html', {'quiz': quiz, 'results': results})


# def quiz_detail(request, quiz_id):
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     return render(request, 'quiz_detail.html', {'quiz': quiz})

# def view_quiz_results(request, quiz_id):
#     quiz = get_object_or_404(Quiz, id=quiz_id)
    
#     # Ensure that only the quiz creator can view the results
#     if request.user != quiz.host:
#         return HttpResponseForbidden("You are not allowed to view these results.")
    
#     results = quiz.results.all().order_by('-score', 'submitted_at')
    
#     return render(request, 'view_quiz_results.html', {'quiz': quiz, 'results': results})

###########################################################################################################333333