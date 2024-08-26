from django.shortcuts import render , redirect
from .models import *
from .utils import *
import random
from django.http import HttpResponseBadRequest
from django.http import JsonResponse

####################################################################################
def quiz_view(request):

    if 'quiz_questions' in request.session:
        quiz_questions = request.session['quiz_questions']
    else:
        level = request.session.get('level')
        subject = request.session.get('subject')
        num_questions = request.session.get('num_questions')

        if subject == "python" :
            if level == "beginner" :
                all_questions = python_easy()
                quiz_questions = random.sample(all_questions, num_questions)
                request.session['quiz_questions'] = quiz_questions
            elif level == "intermediate" :
                all_questions = python_inter()
                quiz_questions = random.sample(all_questions, num_questions)
                request.session['quiz_questions'] = quiz_questions
            elif level == "advance":
                all_questions = python_adv()
                quiz_questions = random.sample(all_questions, num_questions)
                request.session['quiz_questions'] = quiz_questions


        # all_questions = python_easy()
        # quiz_questions = random.sample(all_questions, num_questions)
        # request.session['quiz_questions'] = quiz_questions
        

    context = {
        'questions': quiz_questions
    }
    return render(request, 'ai-show.html', context)
####################################################################################

# def quiz_view(request):
#     # all_questions = load_questions()
#     # all_questions = python_easy()
#     # quiz_questions = random.sample(all_questions, 10)

#     if 'quiz_questions' in request.session:
#         quiz_questions = request.session['quiz_questions']
#     else:
#         all_questions = python_easy()
#         num_questions = request.session.get('num_questions')
#         quiz_questions = random.sample(all_questions, num_questions)
#         request.session['quiz_questions'] = quiz_questions

#     context = {
#         'questions': quiz_questions
#     }
#     return render(request, 'ai-show.html', context)
    # return render(request, 'quiz-v2.html', context)

####################################################################################

def ai_select(request):
    if 'quiz_questions' in request.session:
        del request.session['quiz_questions']

    if request.method == 'POST':
        subject = request.POST.get('subject')
        request.session['subject'] = str(subject)
        level = request.POST.get('level')
        request.session['level'] = str(level)
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


def ai_create_quiz(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        questions = request.POST.getlist('questions')
        options = request.POST.getlist('options')
        correct_options = request.POST.getlist('correct_options')
        image_loc = request.POST.getlist('img')
        quiz = Quiz.objects.create(title=title, host=request.user)
        
        for i in range(len(questions)):
            Question.objects.create(
                quiz=quiz,
                question_text=questions[i],
                option1=options[i*4],
                option2=options[i*4 + 1],
                option3=options[i*4 + 2],
                option4=options[i*4 + 3],
                correct_option=correct_options[i] ,
                image_loc=image_loc[i]
            )
        
        return redirect('quiz_detail', quiz_id=quiz.id)
    

# def quiz_add(request):

#     if request.method == 'post' :
#         level = request.session.get('level')
#         subject = request.session.get('subject')
#         num_questions = 1 

#         if subject == "python" :
#             if level == "beginner" :
#                 all_questions = python_easy()
#             elif level == "intermediate" :
#                 all_questions = python_inter()
#             elif level == "advance":
#                 all_questions = python_adv()

#         add_questions = random.sample(all_questions, num_questions)
#         request.session['add_questions'] = add_questions

#         data = {
#             'questions': add_questions
#         }
#         return JsonResponse(data)


def quiz_add(request):
    # Check if the request method is POST and if it's an AJAX request
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        level = request.session.get('level')
        subject = request.session.get('subject')
        num_questions = 1 

        if subject == "python":
            if level == "beginner":
                all_questions = python_easy()
            elif level == "intermediate":
                all_questions = python_inter()
            elif level == "advance":
                all_questions = python_adv()
            else:
                return JsonResponse({'error': 'Invalid level'}, status=400)

            add_questions = random.sample(all_questions, num_questions)
            request.session['add_questions'] = add_questions

            # Prepare data to send back to JavaScript
            data = {
                'questions': add_questions
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Invalid subject'}, status=400)

    # If the request method is not POST or it's not an AJAX request
    return HttpResponseBadRequest('Invalid request')