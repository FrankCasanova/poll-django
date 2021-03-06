from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Create your views here.


# def index(request):
#     # first we create the funcionality, and then create the connection
#     # the connections are the url's,
#     # there live all connections that activate our functionalities
    
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     # return HttpResponse(template.render(context,request))
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        '''
        Return the last five published questions
        (not including those set to be publisehd in the future)
        '''
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    
    


# def detail(request, question_id):
    
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exist')
#     question = get_object_or_404(Question, pk=question_id) #a number   
    
#     return render(request, 'polls/detail.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        exludes any question that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id) #a number 
#     return render(request, 'polls/result.html', {'question': question})

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #request.POST values are always a string
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'You didn\'t select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    #always return a httpresponseredirect after successfully dealing
    #with POST data. This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,))) #Is so much important to put coma, cuz args must be an iterable.
    
    #reverse function helps avoid having to   hardcode a URL in 
    #the view function. it is given the name of the view that we want to pass control to
    #and the variable portion of the URL pattern that points to that view. in this case,
    #using the URLconf, this reverse() call will return a string like '/polls/3/results/'
    #where the 3 is the value of question.id. This redirected URL will then call the 'result'
    #view to display the final page     
    

