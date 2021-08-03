from django.http import response
from django.shortcuts import render, HttpResponseRedirect
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    
    posts.reverse()

    return render(request,"home.html", {"posts":posts})

def add_post(request):
    usr_name = request.POST["name"]
    dataP = request.POST["data"]

    new_Post = Post(name=usr_name, data=dataP)

    new_Post.save()

    return HttpResponseRedirect("/")

def create_post(request):
    return render(request, "post-from.html")