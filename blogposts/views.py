# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    all_blogposts = Question.objects.all()
    template = 'blogposts/home.html'
    context ={
        'all_blogposts': all_blogposts,
    }
    return render(request, template, context)


# gives you question of that particular id
def post(request, post_id):
    question = Question.objects.get(id=post_id)
    template = 'blogposts/post.html'
    context = {
        'question': question,
    }
    return render(request, template, context)


def hello(request):
    return HttpResponse("<h1>This is the BlogPosts page")

