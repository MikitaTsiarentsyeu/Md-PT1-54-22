import datetime
import email
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Post
from .forms import AddPost, AddPostModelForm
from django.contrib.auth.decorators import permission_required



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
    all_posts = Post.objects.all().order_by('-issued')
    viewed_posts = request.session.get("viewed_posts", [])
    return render(request, 'posts.html', {'posts': all_posts, 'viewed_posts': viewed_posts})

def post(request, id):
    try:
        post = Post.objects.get(id=id)
        viewed_posts = request.session.get("viewed_posts", [])
        if id not in viewed_posts:
            viewed_posts.append(id)
        request.session["viewed_posts"] = viewed_posts
    except:
        post = ""
    return render(request, 'post.html', {'post': post})

@permission_required('app.add_post')
def add_post(request):

    if request.method == 'POST':
        new_form = AddPost(request.POST, request.FILES)

        if new_form.is_valid():
            post = Post()
            post.author = Author.objects.get(email=request.user.email)
            post.issued = datetime.datetime.now()
            post.title = new_form.cleaned_data['title']
            post.subtitle = new_form.cleaned_data['subtitle']
            post.content = new_form.cleaned_data['content']
            post.post_type = new_form.cleaned_data['post_type']
            post.image = new_form.cleaned_data['image']
            post.save()

            return redirect('posts')
            
    elif request.method == "GET":
        new_form = AddPost()

    return render(request, 'add_post.html', {'new_form': new_form})

def add_post_model_form(request):

    if request.method == 'POST':
        new_form = AddPostModelForm(request.POST, request.FILES)

        if new_form.is_valid():
            post = new_form.save(commit=False)
            post.author = Author.objects.all()[0]
            post.issued = datetime.datetime.now()

            post.save()
            new_form.save_m2m()

            return redirect('posts')
            
    elif request.method == "GET":
        new_form = AddPostModelForm()

    return render(request, 'add_post.html', {'new_form': new_form})