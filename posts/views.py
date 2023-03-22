from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
from .models import Comment, Post
from django.contrib.auth.decorators import login_required


# The following function is used to increase the post viewed based on session key of the user
def viewed_by_session_count(request, obj):
    session_key = 'viewed_{}'.format(obj.post_id)
 
    if not request.session.get(session_key, False):
        obj.post_view_count += 1
        obj.save(update_fields=['post_view_count'])
        request.session[session_key] = True


def show_post(request, post_slug):
    post = Post.objects.filter(post_slug=post_slug).first() # Filtering the post based on post slug and getting the first post from it
    if post: # if post exist
   
        post_comments = Comment.objects.filter(
            comment_post=post.post_id).order_by('comment_created_at') # getting the comments for the post
        post_liked = False

        if request.user.is_authenticated: # if user is logged in
          

            if post.post_likes.filter(id=request.user.id).exists(): # if user likes the post
                post_liked = True

        context = {
            "post": post,
            "post_liked": post_liked,
            "post_comments": post_comments,
      
        }
        viewed_by_session_count(request, post) #  function increment the post 
        return render(request, "post/show.html", context)
    else: # if post does not exist
        return redirect("home")  # redirecting to home

@login_required(login_url="/") # login_required() is a decorator used to check whether user logged in or not else redirect them to login page
def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid(): # checking if the form is valid or not
        new_post = form.save(commit=False) # saving the form but not commiting it to the database yet
        form.instance.post_created_by = request.user # getting the user and storing it to the post created by.

        new_post.save() # saving the post
        form.save_m2m() # saving the form  and saving it to database
        messages.success(request, "Post created succesfully") # success message as the post created successfully
        return redirect("home") # returning to home page
    context = { # passing the form for post creation to the html page
        "form": form
    }
    return render(request, 'post/create.html', context)


def create_comment(request):
    if request.method == "POST":# checking if the request method is POST
        post_slug = request.POST['post_slug'] # getting the post slug from html form
        comment_post = Post.objects.get(post_slug=post_slug) # getting the post to be commented based on post_slug
        if comment_post: # if the post exists
            comment_content = request.POST['comment_content'] # getting the comment
            comment_user = request.user # getting the user who commented 
            new_comment = Comment(comment_content=comment_content, 
                                  comment_user=comment_user, comment_post=comment_post)# creating the comment
            new_comment.save() # saving the comment into the database

            return redirect("show_post", post_slug) # returning to the post that user commented

    return redirect("home") # if no such post exist then redirect to home

def show_category_posts(request,category_id):
    # Shows the Posts in a category based on category Id
    posts = Post.objects.filter(post_category=category_id).order_by("-post_created_at")
    context = {
        "posts":posts,
          'colors': ['primary', 'secondary', 'success', 'danger', 'warning', 'info'],
        
    }
    return render(request,"category/show.html",context)

def like_post(request, post_slug):
    post = Post.objects.get(post_slug=post_slug)
    if request.method == "POST" and post:
        if request.user.is_authenticated:
            user = request.user
            if post.post_likes.filter(id=user.id).exists():
                post.post_likes.remove(user)
                return redirect("show_post", post_slug)
            else:
                post.post_likes.add(user)
                return redirect("show_post", post_slug)
def delete_post(request):
    if request.method == "POST": # Checking if the request is POST or NOT
        post_slug = request.POST['post_slug'] # Getting the post slug

        if request.user.is_authenticated:
            post = Post.objects.filter(post_slug=post_slug).first()
            if post.post_created_by == request.user:
                post.delete()
                messages.success(request,"Successfully deleted the post")
                return redirect("home")
            else:
                messages.error(request,"Something went wrong when deleting the post")
    return redirect("home")
        