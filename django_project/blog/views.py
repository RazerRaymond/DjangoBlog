from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Comment,Category,Archive,Like,Dislike
from .forms import CommentForm,BlogForm
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts':posts,
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'}) 

def category(request,category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-date_posted')
    context = {
        'category':category,
        'posts':posts
    }
    return render(request,"blog/category.html",context)
@login_required
def blog_detail(request,pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = request.user,
                content = form.cleaned_data["content"],
                post = post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post":post,
        "comments":comments,
        "form":form,
    }
    return render(request,"blog/blog_detail.html",context)
@login_required
def create(request):
    form = BlogForm()
    if request.method=='POST' :
        form = BlogForm(request.POST)
        if(form.is_valid()):
            post = Post.objects.create(
                title = form.cleaned_data["title"],
                content = form.cleaned_data["content"],
                author = request.user,
            )
            post.save()
            return redirect("/")
            # post.categories.add(form.cleaned_data["categories"])
    context = {
        "form":form
    }
    return render(request,"blog/createNewPost.html",context)

def delete(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts':posts,
    }
    return render(request,'blog/home.html',context)

def edit(request,pk):
    post = Post.objects.get(pk=pk)
    form = BlogForm(request.POST,instance=post)
    if request.method=='POST' :
        if(form.is_valid()):
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect("/")
            # post.categories.add(form.cleaned_data["categories"])
    context = {
        "form":form
    }
    return render(request,"blog/editPost.html",context)
@login_required
def archive(request,pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    newarchive = Archive.objects.create(
        post = post,
        user = user
    )
    newarchive.save()
    return redirect("/")
@login_required
def archived(request):
    user = request.user
    archives = Archive.objects.values_list('post', flat=True).filter(user=user)
    posts = Post.objects.filter(pk__in=set(archives))
    context = {
        "posts":posts
    }
    return render(request,"blog/archivePost.html",context)

def unarchive(request,pk):
    post = Post.objects.get(pk=pk)
    archive = Archive.objects.filter(post=post,user=request.user)
    archive.delete()
    user = request.user
    archives = Archive.objects.values_list('post', flat=True).filter(user=user)
    posts = Post.objects.filter(pk__in=set(archives))
    context = {
        "posts":posts
    }
    return render(request,"blog/archivePost.html",context)
@login_required
def like(request,pk):
    post = Post.objects.get(pk=pk)
    archive = Like.objects.filter(post=post,user=request.user)
    if archive.count() == 0:
        like = Like.objects.create(
            post = post,
            user = request.user 
        )
        like.save()
        old = Post.objects.get(pk=pk)
        old.likes = old.likes + 1
        old.save()
    
    return redirect("/")
@login_required
def dislike(request,pk):
    post = Post.objects.get(pk=pk)
    archive = Dislike.objects.filter(post=post,user=request.user)
    if archive.count() == 0:
        dislike = Dislike.objects.create(
            post = post,
            user = request.user 
        )
        dislike.save()
        old = Post.objects.get(pk=pk)
        old.dislikes = old.dislikes + 1
        old.save()
    
    return redirect("/")
    