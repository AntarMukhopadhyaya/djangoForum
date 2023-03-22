# The Following view Handles the User Registration , Login and Logout

from django.shortcuts import redirect # used to redirect to specified page
from django.contrib.auth.models import User # Importing user model which stores the users data and used to create user
from django.contrib.auth import logout # used to logout the user 
from django.contrib.auth import authenticate,login # authenticate function is used to check whether the username and user password are valid 
#login function is used to login the user
from django.contrib import messages # messages are used to send messages across html pages 



def user_register(request):
    if request.method == 'POST': # Checking if the request method is Post or not
        user_name = request.POST['user_name'] # getting user name from html form
        user_email = request.POST['user_email']# getting user email from html form
        user_password = request.POST['user_password']# getting user password from html form
        user_confirm_password = request.POST['user_confirm_password']# getting user confirm password from html form
        if user_password != user_confirm_password: # Checking if user password is not equals to  user confirm password
            messages.error(request,"Password and Confirm password should be equal") # Throwing an error messages as both password should match
            return redirect("home") # redirecting to home
        elif user_name and user_email and user_password and user_password and user_confirm_password: # Checking if all the required fields exist or not
            if User.objects.filter(username=user_name).exists(): # Checking if user with same username already exist or not
                messages.error(request,"Username already exists.") # if exist throwing an error message that user exists
                return redirect("home") # redirecting to home
            elif User.objects.filter(email=user_email).exists(): #Checking if user with same email already exists or not
                messages.error(request,"Email already exists.") # if exist throwing an error message that user exists
                return redirect("home")# redirecting to home
            else: # Else we create the user with username, email and password obtained from the html form
                user = User.objects.create_user(username=user_name,email=user_email,password=user_password) #User is the special class called model we are using create_user
                #method to create the user
                user.save() # saving the message
                messages.success(request,"User successfully created.") # giving success message
                return redirect('home') # redirecting to home
        elif len(user_password) < 8: # if password length < 8 then throw error message saying password length must be greater
            messages.error(request,"Password must be greater than 8 characters")
            return redirect('home') # redirecting to home

def user_login(request): 
    if request.method == 'POST': # checking if the request method is post
        user_name = request.POST['user_name'] # Getting the user name form the html form
        user_password = request.POST['user_password'] # getting the user password from the html

        user = authenticate(username=user_name,password=user_password) # authenticating user based on username
        # and password obtained from html form
        if user is not None: # checking if user exist or not
            login(request,user) # if user exists login the user in to his/her account
            
            return redirect('home') # redirect to home page
        else: # Password or username is wrong
            messages.error(request,'Invalid Credentials')  # sending an error message to home page
            redirect('home') # redirecting to home page
    return redirect("home") # redirecting to home page

def user_logout(request):
    if request.user.is_authenticated: # Checking if user logged in or not
        logout(request) # logging out the user from his/her account  logout() function is a inbuilt django function obtained from 
        # django.contrib.auth 
        messages.success(request,"Successfully Logged out from the account") # Sending a message saying user has successfully logged out
        return redirect("home") # redirecting to home


