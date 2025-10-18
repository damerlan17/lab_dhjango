from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def create_post(request):
    if request.method == "POST":
        post = Post()
        post.title = request.POST.get("title")
        post.detail = request.POST.get("detail")
        post.save()
        return HttpResponseRedirect("/posts")
    else:
        postform = PostForm()
        return render(request, "create_post.html", {"form": postform})
