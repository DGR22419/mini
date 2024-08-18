from django.shortcuts import render, redirect
from django.contrib.auth import login , authenticate
from .forms import StudentSignUpForm, TeacherSignUpForm
from .models import *
from q.models import *
from .forms import CustomLoginForm
from django.contrib.auth.decorators import login_required

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_home')
    else:
        form = StudentSignUpForm()
    return render(request, 'signup.html', {'form': form, 'user_type': 'Student'})

def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('teacher_home')
    else:
        form = TeacherSignUpForm()
    return render(request, 'signup.html', {'form': form, 'user_type': 'Teacher'})

# def login_view(request):
#     # Handle login logic here
#     if request.user.is_authenticated:
#         if request.user.is_student:
#             return redirect('student_home')
#         elif request.user.is_teacher:
#             return redirect('teacher_home')
#     return render(request, 'login.html')

def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_student:
                    return redirect('student_home')
                elif user.is_teacher:
                    return redirect('teacher_home')
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {'form': form})

def root(request):
    return render(request , 'landing.html')

# @login_required
# def home_view(request):
#     user = request.user
#     quiz = Quiz.objects.filter(host=user)
#     result = QuizResult.objects.filter(user=user)
#     return render(request, 'dashboard.html', {'quizzes': quiz, 'results': result})
#     # return render(request, 'dashboard.html')

@login_required
def home_std(request):
    user = request.user
    result = QuizResult.objects.filter(user=user)
    return render(request, 'dashboard_std.html', {'results': result})
    # return render(request, 'dashboard.html')

@login_required
def home_tea(request):
    user = request.user
    quiz = Quiz.objects.filter(host=user)
    return render(request, 'dashboard_tea.html', {'quizzes': quiz})
    # return render(request, 'dashboard.html')