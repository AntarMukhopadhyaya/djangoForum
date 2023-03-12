from django.shortcuts import render,redirect
from django.contrib import messages
from django.template.defaultfilters import slugify
from .forms import PostForm,CommentForm
from  .models import Comment,Post
# Create your views here.
def show_post(request,post_slug):
    post = Post.objects.get(post_slug=post_slug)
    post_comments = Comment.objects.filter(comment_post=1).order_by('comment_created_at')
    post_liked = False
    if request.user.is_authenticated:

        if post.post_likes.filter(id= request.user.id).exists():
            post_liked= True

 
    context = {
    "post": post,
    "post_liked":post_liked,
    "post_comments" : post_comments
    }
    return render(request,"post/show.html",context)

def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        new_post = form.save(commit=False)
        form.instance.post_created_by = request.user
        # form.instance.post_slug = slugify(request.post_title)

        new_post.save()
        form.save_m2m()
        messages.success(request,"Post created succesfully")
        return redirect("home")
    context = {
        "form": form
    }
    return render(request,'post/create.html',context)


def create_comment(request):
    if request.method == "POST":
        post_slug  = request.POST['post_slug']
        comment_post = Post.objects.get(post_slug=post_slug)
        if comment_post:
            comment_content = request.POST['comment_content']
            comment_user = request.user
            new_comment = Comment(comment_content=comment_content,comment_user=comment_user,comment_post=comment_post)
            if new_comment.save():
                return redirect("show_post",post_slug)
            else:
                messages.error(request,"Something went wrong please try again")
                return redirect("show_post",post_slug)

    return redirect("home")

def like_post(request,post_slug):
    post = Post.objects.get(post_slug=post_slug)
    if request.method == "POST" and post:
        if request.user.is_authenticated:
            user = request.user
            if post.post_likes.filter(id=user.id).exists():
                post.post_likes.remove(user)
                return redirect("show_post",post_slug)
            else:
             post.post_likes.add(user)
             return redirect("show_post",post_slug)

