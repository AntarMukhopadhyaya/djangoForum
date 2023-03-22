
from django.shortcuts import redirect, render, get_object_or_404
from posts.models import Category, Post
from django.contrib.auth.models import User
from django.db.models import Count
from taggit.models import Tag


def home(request):
    # Getting the posts based on when they were created
    posts = Post.objects.all().order_by('-post_created_at')
    # Getting the newest user based on date joined
    newest_user = User.objects.all().order_by("-date_joined").first()

    # Fetching the categories based on when they were created
    categories = Category.objects.all().order_by('category_created_at')
    favourite_posts = Post.objects.order_by(
        '-post_view_count')[:5]  # Only getting the top viewed posts
    post_count = Post.objects.all().count()  # Counting the number of posts
    user_count = User.objects.all().count()  # Counting the total number of users
    # Counting the total number of categories
    category_count = Category.objects.all().count()
    context = {
        "posts": posts,
        "categories": categories,
        "post_count": post_count,
        "favourite_posts": favourite_posts,
        "user_count": user_count,
        "category_count": category_count,
        "newest_user":newest_user,
        'colors': ['primary', 'secondary', 'success', 'danger', 'warning', 'info'],
    }
    return render(request, 'home.html', context)


def search(request):
    # Getting the search query from the urls
    search_query = request.GET['search_query']
    print(search_query)
    # Filtering the post by checking the post
    posts = Post.objects.filter(post_title__icontains=search_query)
    # which contains the  post title same as the search query
    
    context = {  # Context is a  dictionary variable that stores all the variables that we will pass to the specified page

        "posts": posts,
        "search_query": search_query,
        'colors': ['primary', 'secondary', 'success', 'danger', 'warning', 'info'],
    }
    # Rendering then search.html page with context variable
    return render(request, 'search.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(post_tags=tag).order_by("-post_created_at")
    context = {
        'posts': posts,
        "tag": tag,
        'colors': ['primary', 'secondary', 'success', 'danger', 'warning', 'info'],

    }
    return render(request, 'tagged.html', context)
