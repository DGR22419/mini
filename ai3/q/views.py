from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse , HttpResponseForbidden
import re
import os

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

#     return render(request, 'quiz-v2.html')

#################################################################################################################try


@login_required
def create_quiz(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        questions = request.POST.getlist('questions')
        options = request.POST.getlist('options')
        correct_options = request.POST.getlist('correct_options')
        images = request.FILES.getlist('images')  # Get list of uploaded image files

        print("Images received:", images)

        quiz = Quiz.objects.create(title=title, host=request.user)
        
        for i in range(len(questions)):
            # Handle image file saving
            # image_file = images[i] if len(images) > i else None
            # image_path = None
            
            # if image_file:
            #     # fs = FileSystemStorage(location=os.path.join('static', 'questions'))  # Define storage location
            #     # image_path = fs.save(image_file.name, image_file)  # Save image file
            #     fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'questions'))  # Save images in MEDIA_ROOT
            #     image_path = fs.save(image_file.name, image_file)

            image_file = images[i] if i < len(images) else None

            # Create Question object
            Question.objects.create(
                quiz=quiz,
                question_text=questions[i],
                option1=options[i * 4],
                option2=options[i * 4 + 1],
                option3=options[i * 4 + 2],
                option4=options[i * 4 + 3],
                correct_option=correct_options[i],
                images=image_file  # Save the path to the image field
            )

        
        return redirect('quiz_detail', quiz_id=quiz.id)

    return render(request, 'quiz-v2.html')


#################################################################################################################

# def join_quiz(request, code):
#     quiz = get_object_or_404(Quiz, code=code)
    
#     if request.method == 'POST':
#         user_answers = request.POST.getlist('answers')
#         score = 0
#         for i, question in enumerate(quiz.questions.all()):
#             if question.correct_option == user_answers[i]:
#                 score += 1
        
#         QuizResult.objects.create(quiz=quiz, user=request.user, score=score)
        
#         return redirect('quiz_result', quiz_id=quiz.id)
    
#     return render(request, 'join_quiz.html', {'quiz': quiz})

# @login_required
# def join_quiz(request, code):
#     quiz = get_object_or_404(Quiz, code=code)
#     questions = quiz.questions.all()

#     if request.method == 'POST':
#         score = 0
#         for question in questions:
#             selected_option = request.POST.get(str(question.id))  # Get selected option for this question
#             if selected_option and selected_option == question.correct_option:
#                 score += 1

#         # Save the score to the database, or pass it to the template
#         # For simplicity, we're just returning the score here
#         return render(request, 'quiz_result.html', {'quiz': quiz.id, 'score': score})

#     return render(request, 'join_quiz.html', {'quiz': quiz, 'questions': questions})


# @login_required
# def join_quiz(request, code):
    # quiz = get_object_or_404(Quiz, code=code)
    
    # if request.method == 'POST':
    #     # user_answers = request.POST.getlist('answers')
    #     user_answer = request.POST.get(f'answers_{question.id}')
    #     score = 0
        
    #     # Make sure the length of user answers matches the number of questions
    #     questions = quiz.questions.all()
        
    #     for i, question in enumerate(questions):
    #         try:
    #             if question.correct_option == user_answers[i]:
    #                 score += 1
    #         except IndexError:
    #             # Handle the case where there are fewer answers than questions
    #             continue
        
    #     # Store the quiz result for the user
    #     QuizResult.objects.create(quiz=quiz, user=request.user, score=score)
        
    #     return redirect('quiz_result', quiz_id=quiz.id)
    
    # return render(request, 'join_quiz.html', {'quiz': quiz})

@login_required
def join_quiz(request, code):
    quiz = get_object_or_404(Quiz, code=code)
    
    if request.method == 'POST':
        score = 0
        user_answers = {}
        questions = quiz.questions.all()
        total_questions = questions.count()
        
        for question in questions:
            user_answer = request.POST.get(f'answers_{question.id}')
            user_answers[question.id] = user_answer  # Store user answer

            if user_answer and user_answer == question.correct_option:
                score += 1
        
        # Store the quiz result for the user
        QuizResult.objects.create(quiz=quiz, user=request.user, score=score)

        # Store data in the session to be accessed in the result view
        request.session['score'] = score
        request.session['total_questions'] = total_questions
        request.session['user_answers'] = user_answers
        
        return redirect('quiz_result', quiz_id=quiz.id)
    
    return render(request, 'join_quiz.html', {'quiz': quiz})




@login_required
def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    score = request.session.get('score')
    total = request.session.get('total_questions')
    user_answers = request.session.get('user_answers', {})
    
    questions = quiz.questions.all()
    detailed_results = []

    for question in questions:
        correct_answer = question.correct_option
        user_answer = user_answers.get(str(question.id))
        
        detailed_results.append({
            'question': question.question_text,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'options': {
                'option1': question.option1,
                'option2': question.option2,
                'option3': question.option3,
                'option4': question.option4,
            }
        })

    return render(request, 'result.html', {
        'quiz': quiz,
        'score': score,
        'total': total,
        'detailed_results': detailed_results
    })


# @login_required
# def quiz_result(request, quiz_id):
#     quiz = get_object_or_404(Quiz, id=quiz_id)
#     # results = quiz.results.all()

#     # score = request.session.pop('score', None)
#     score = request.session.get('score')
#     total = request.session.get('total_questions')

#     return render(request, 'result.html', {'quiz': quiz, 'score': score, 'total': total})

def view_questions(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.all()

    return render(request, 'view_questions.html', {
        'quiz': quiz,
        'questions': questions,
    })



@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    results = quiz.results.all()
    return render(request, 'quiz_detail_v2.html', {'quiz': quiz , 'results': results})

@login_required
def view_quiz_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    # Ensure that only the quiz creator can view the results
    if request.user != quiz.host:
        return HttpResponseForbidden("You are not allowed to view these results.")
    
    results = quiz.results.all().order_by('-score', 'submitted_at')
    
    return render(request, 'view_quiz_results.html', {'quiz': quiz, 'results': results})

# @login_required
# def join_room(request):
#     return render(request, 'room.html')


# def join_room(request):
#     if request.method == 'POST':
#         room_code = request.POST.get('room_code')
#         if room_code:
#             # Check if the room code exists in the QuizRoom model
#             if Quiz.objects.filter(code=room_code).exists():
#                 return redirect('join_quiz', code=room_code)
#             else:
#                 # If the room code does not exist, show an error
#                 return render(request, 'room.html', {'error': 'Room not found.'})
#     return render(request, 'room.html')

@login_required
def join_room(request):
    if request.method == 'POST':
        room_code = request.POST.get('room_code')
        if room_code:
            # Validate that the room code contains only digits
            if not re.match(r'^\d+$', room_code):
                return render(request, 'room.html', {'error': 'Invalid room code. Only numbers are allowed.'})

            # Check if the room code exists in the Quiz model
            if Quiz.objects.filter(code=room_code).exists():
                return redirect('join_quiz', code=room_code)
            else:
                # If the room code does not exist, show an error
                return render(request, 'room.html', {'error': 'Room not found.'})
    return render(request, 'room.html')

@login_required
def delete_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == "POST":
        quiz.delete()
        return redirect('teacher_home') 
    return render(request, 'delete_confirm.html', {'object': quiz, 'type': 'quiz'})

@login_required
def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    results = quiz.results.all()
    return render(request, 'view.html', {'quiz': quiz , 'results': results})