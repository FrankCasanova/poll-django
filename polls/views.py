from polls.models import Question
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response
from django.template import loader
from django.http import Http404

# Create your views here.


def index(request):
    # first we create the funcionality, and then create the connection
    # the connections are the url's,
    # there live all connections that activate our functionalities
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'polls/index.html', context)
    
    
    
    


def detail(request, question_id):
    
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)    
    
    return render(request, 'polls/detail.html', {'question': question})


def result(request, question_id):
    response = f'your\'re looking at the resutls of question {question_id}'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse(f'Your\'re voting on question {question_id}')