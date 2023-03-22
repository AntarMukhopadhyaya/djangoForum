# In the following urls.py we have defined the routes/endpoint for user registration,login and logout


from django.urls import path # Path is used to generate the endpoint it takes 3 parameters 1) endpoint 2) callback function 3)endpoint name
from . import views # We are importing the views.py so that we can use the function for corresponding routes
urlpatterns = [
    # Post Routes
    path("register",views.user_register,name='user_register'), # url for user registration
    path('logout',views.user_logout,name="user_logout"), #url for logout
    path("login",views.user_login,name="user_login"), # url for login

]