
from django.urls import path
from . import views
urlpatterns = [
    # Post Routes
    path("show_post/<slug:post_slug>",views.show_post,name="show_post"), # url for showing the post based on its slug
    path("create",views.create_post,name="create_post"), # url for creating the post
    path("like_post/<slug:post_slug>",views.like_post,name="like_post"), # url for liking the post based on its post slug
    path("delete_post/",views.delete_post,name="delete_post"),
    path("category/<int:category_id>",views.show_category_posts,name="show_category_posts"), #url for showing the category based on its id
    path("comment/create",views.create_comment,name='create_comment') # urll for creating the comment

]
