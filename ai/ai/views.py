from django.shortcuts import render , redirect
from .models import *
from .utils import *
import random
from django.http import HttpResponseBadRequest



def quiz_view(request):
    # all_questions = load_questions()
    # all_questions = python_easy()
    # quiz_questions = random.sample(all_questions, 10)

    if 'quiz_questions' in request.session:
        quiz_questions = request.session['quiz_questions']
    else:
        # Load questions using python_easy() function
        all_questions = python_easy()
        
        num_questions = request.session.get('num_questions')

        # Select 10 random questions
        quiz_questions = random.sample(all_questions, num_questions)
        
        # Save the questions in the session
        request.session['quiz_questions'] = quiz_questions

    context = {
        'questions': quiz_questions
    }
    return render(request, 'ai-show.html', context)
    # return render(request, 'quiz-v2.html', context)

def ai_select(request):
    if 'quiz_questions' in request.session:
        del request.session['quiz_questions']

    if request.method == 'POST':
        subject = request.POST.get('subject')
        level = request.POST.get('level')
        num_questions = request.POST.get('num')
        if num_questions:
            try:
                num_questions = int(num_questions)
                request.session['num_questions'] = num_questions
                return redirect('ai_quiz')
            except ValueError:
                # Handle invalid integer conversion
                return HttpResponseBadRequest("Invalid number of questions")
        else:
            # Handle missing 'num' field
            return HttpResponseBadRequest("Number of questions not provided")

    return render(request, 'ai-generated.html')


# def ai_select(request):
#     if 'quiz_questions' in request.session:
#         del request.session['quiz_questions']

#     if request.method == 'POST':
#         num_questions = request.GET.get('num' )
#         # num_questions = int(num_questions)
#         print(int(num_questions))
#         request.session['num_questions'] = int(num_questions)
#         return redirect('ai_quiz')
    
#     # subject = request.GET.get('subject', '')
#     # difficulty = request.GET.get('difficulty', '')
    

    
#     return render(request , 'ai-generated.html')
