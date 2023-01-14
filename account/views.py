from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong Username or Password')
    context = {
        'messages': messages,
    }
    return render(request, 'account/login.html', context)


def registerUser(request):
    if request.method == 'GET':
        return render(request, 'account/register.html')
    else:
        user_form = UserCreationForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.email = request.POST.get('email')
            profile = Profile(user=user)
            user.save()
            profile.save()
            login(request, user)
            return redirect('profile-update')
        else:
            context = {
                'user_form': user_form,
                'messages': messages,
            }
            return render(request, 'account/register.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')