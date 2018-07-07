# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    all_blogposts = Question.objects.all()
    template = loader.get_template('blogposts/home.html')
    context ={
        'all_blogposts': all_blogposts,
    }

    return HttpResponse(template.render(context, request))

def hello(request):
    return HttpResponse("<h1>This is the BlogPosts page")

