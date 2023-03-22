
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls), #url for admin included in django by default
    path("",views.home,name="home"), #url for home page
    path("search",views.search,name="search"), #url for search page
    path("tagged/<slug:slug>",views.tagged,name="tagged"), # user for tagged page
    path("post/",include('posts.urls')), # including the urls of posts app
    path("user/",include('users.urls')), #including the urls of users app
]
