from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import Question,Choice
# Create your views here.


#use loader
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'lastest_question_list':latest_question_list
#     }
#     return HttpResponse(template.render(context,request))

#use render (common use)
def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lastest_question_list':lastest_question_list}
    return render(request,'polls/index.html',context)


def detail(request,question_id):
    #stander use Http404
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')

    #common use 404
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def result(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        # redisplay the question vote form.
        return render(request,'polls/detail.html',{'question':question,
                            'error_message':"You did't select choice"
                            })
    else:
        select_choice.votes += 1
        select_choice.save()
    return HttpResponseRedirect(reverse('polls:result',args=(question.id,)))



