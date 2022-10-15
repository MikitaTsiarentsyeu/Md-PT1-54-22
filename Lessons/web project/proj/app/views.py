import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    return render(request, 'home.html')

# def posts(request):
#     posts = Post.objects.all()
#     post_list = ""
#     for post in posts:
#         post_list += f"<li><h3>{post.title}</h3><p>by {post.author.name}</p></li>"
#     response = f"<h1>Posts:</h1><ul>{post_list}</ul>"
#     return HttpResponse(response)

# def post(request, id):
#     try:
#         post = Post.objects.get(id=id)
#         response = f"<h3>{post.title}</h3><p>{post.content}</p><p>by {post.author.name}</p>"
#     except:
#         response = "<h2>the post with such id was not found</h2>"
#     return HttpResponse(response)

def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': all_posts})

def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        post = ""
    return render(request, 'post.html', {'post': post})