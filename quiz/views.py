from random import uniform
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader

from .models import Question, ANSWER, Result


correct_aswers = []

def result(request):

    important_keys = [a for a in list(request.GET) if not(a=='csrfmiddlewaretoken')]
    user_answers = [int(request.GET[key]) for key in important_keys]

    global correct_aswers
    print(user_answers)
    print(correct_aswers)

    result = 0

    for i in range(0,10):
        if user_answers[i]==correct_aswers[i]:
            result=10+result

    print(result)
    temp = loader.get_template('quiz/test.html')
    context = {
            'result' : result,
                }
    r = Result.objects.create(result=result, user_id=request.user, date=timezone.now())
    r.save()

    return HttpResponse(temp.render(context, request))


def language(request):
    return render_to_response('quiz/quiz_index.html')


def quiz(request):


    language = request.GET['lang']
    level = request.GET['level']

    print(language, level)
    #for s in range(10):
    temp = loader.get_template('quiz/quiz.html')

    context = {'questions' : []}

    tmp = [a for a in Question.objects.all().filter(Q_LANGUAGE=language).filter(Q_LEVEL=level).values('id')]
    questions_id = list(map(lambda x:x['id'], tmp))

    global correct_aswers
    correct_aswers = []

    from numpy.random import choice

    for i in range(10):
        ids = list(choice(questions_id, size=4, replace=False))
        correct_id = ids[round(uniform(0, 3))]

        correct_aswers.append(correct_id)

        question = Question.objects.all().filter(id=correct_id).values().first()['Q_CONTENT']

        answer_1 = ANSWER.objects.all().filter(question_id=ids[0]).values().first()['A_CONTENT_C']
        answer_2 = ANSWER.objects.all().filter(question_id=ids[1]).values().first()['A_CONTENT_C']
        answer_3 = ANSWER.objects.all().filter(question_id=ids[2]).values().first()['A_CONTENT_C']
        answer_4 = ANSWER.objects.all().filter(question_id=ids[3]).values().first()['A_CONTENT_C']
        id_1 = ANSWER.objects.all().filter(question_id=ids[0]).values().first()['question_id']
        id_2 = ANSWER.objects.all().filter(question_id=ids[1]).values().first()['question_id']
        id_3 = ANSWER.objects.all().filter(question_id=ids[2]).values().first()['question_id']
        id_4 = ANSWER.objects.all().filter(question_id=ids[3]).values().first()['question_id']

        print(ids)
        context['questions'].append({
                'question': question,
                'answer_1': answer_1,
                'answer_2': answer_2,
                'answer_3': answer_3,
                'answer_4': answer_4,
                'id_1': id_1,
                'id_2': id_2,
                'id_3': id_3,
                'id_4': id_4,
            })


    return HttpResponse(temp.render(context, request))
