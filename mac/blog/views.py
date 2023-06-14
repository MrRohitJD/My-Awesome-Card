from django.shortcuts import render
from .models import BlogPost
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    post = BlogPost.objects.all()
    print(post)
    param = {'posts':post}
    return render(request,'blog/index.html',param)

def blogpost(request,id):
    post = BlogPost.objects.filter(post_id = id)[0]
    all = BlogPost.objects.all()
    param = {'posts':post,'all':all}
    return render(request, 'blog/blogpost.html',param)
