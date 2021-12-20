from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import *
import uuid

# Create your views here.
def home(request):
    return render(request, 'Account/home.html')

def handleLogin(request):
    if request.method == 'POST':
        # email=request.POST.get('email')
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpassword')

        user_obj = User.objects.filter(username=username).first()

        if user_obj is None:
            messages.error(request, 'User not found')
            return redirect('/login')
        else:
            profile_obj = Profile.objects.filter(user=user_obj).first()
            if not profile_obj.is_verified:
                messages.error(request, 'Your account is not verified. Please check your mailbox')
                return redirect('/login')

            user = authenticate(request, username=username, password=password)
                
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.success(request, 'Invalid credentials')
                return redirect('/login')
        
    return render(request, 'Account/login.html')

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        roll_number = request.POST['roll_number']
        phone_number = request.POST['phone_number']
        branch = request.POST['branch']
        year = request.POST['year']

        try:
            # Username 
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Username already exists')
                return redirect('/signup')

            if not username.isalnum():
                messages.error(request, 'Username should only contains letters & numbers')
                return redirect('/signup')

            if len(username) > 10:
                messages.error(request, 'Username must be under 10 characters')
                return redirect('/signup')

            # First name
            if not fname.isalpha():
                messages.error(request, 'first name must contain only characters')
                return redirect('/signup')
        
            # Last name
            if not lname.isalpha():
                messages.error(request, 'Last name must contain only characters')
                return redirect('/signup')

            # Email
            if User.objects.filter(email=email).exists():
                messages.success(request, 'Email already exists')
                return redirect('/signup')

            if not email.endswith('@gmail.com'):
                messages.error(request, 'Email must be a gmail account')
                return redirect('/signup')

            # Password
            if pass1 != pass2:
                messages.error(request, 'Passwords do not match')
                return redirect('/signup')
            if len(pass1) < 5:
                messages.error(request, 'Password is too short')
                return redirect('/signup')


            # Create User
            user_obj = User.objects.create_user(username=username, email=email, password=pass1)
            user_obj.first_name = fname
            user_obj.last_name = lname
            user_obj.save()

            auth_token = str(uuid.uuid4())
            # Create Profile

            profile_obj = Profile.objects.create(user=user_obj,fname=fname,lname=lname,email=email,roll_number=roll_number,phone_number=phone_number,branch=branch, year=year, auth_token = auth_token)
            profile_obj.save()
            
            send_authentication_mail(username, email, auth_token)
            # messages.success(request, 'Please check your email to verify your account')
            return redirect('/token')

        except Exception as e:
            print(e)
    # else:
    #     return HttpResponse('404 - Not Found')

        # print("POST")
        # print(request.POST)
        # return render(request, 'Account/success.html')
    return render(request, 'Account/signup.html')

def token(request):
    return render(request, 'Account/token.html')

def success(request):
    return render(request, 'Account/success.html')

def send_authentication_mail(username, email, auth_token):
    subject = "Verify your Gurukul Account"
    message = f"Hi {username}, \n\t Thanks for getting started with Gurukul!\nWe need a little more information to complete your registration, including a confirmation of your email address. \n\nClick below to confirm your email address:\n\n{settings.BASE_URL}/verify/{auth_token} \n\nIf you have problems, please paste the above URL into your web browser.\n\nWelcome to Gurukul! \nTeam Gurukul"
    from_email = settings.EMAIL_HOST_USER
    to_list = [email]
    print(f"From: {from_email},\nTo: {to_list},\nSubject: {subject},\nMessage: {message}, ")
    send_mail(subject, message, from_email, to_list, fail_silently=False)

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Account already verified')
                return redirect('/login')
            else:
                profile_obj.is_verified = True
                profile_obj.save()
                messages.success(request, 'Your account has been verified successfully')
                return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        messages.success(request, 'Something went wrong')

def error(request):
    return render(request, 'Account/error.html')

# @login_required(login_url='/login')
def handleLogout(request): 
    # With Proper Authentication
    if request.method == 'GET':
        logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('home')
    # Means Direct Site Access
    return HttpResponse('404 - Not Found')