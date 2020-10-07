from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'lastest_question_list':latest_question_list
    }
    return HttpResponse(template.render(context,request))


def detail(request,question_id):
    return HttpResponse(f'Looking question at {question_id}')

def result(request,question_id):
    return HttpResponse(f'Looking result at {question_id}')

def vote(request,question_id):
    return HttpResponse(f'Votting at {question_id}')
