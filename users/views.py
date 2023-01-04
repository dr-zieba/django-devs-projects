from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    #profile skills with description
    topSkills = profile.skill_set.exclude(description__exact="")

    #profile skill without description
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)

def loginUser(request):
    page = 'login'
    context = {'page': page}
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            #check if user exists in db
            user = User.objects.get(username=username)
        except Exception as e:
            messages.error(request, f'User not found. Exception: {e}')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User logged in')
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password incorrect')

    return render(request, 'users/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, 'User logout')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # commit false creates an instance but do not save it at that point
            # it is possible to modify data and then save it
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User created')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'error')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)
