from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth


def signup(request):
    if request.user.is_authenticated:
        return render(request, 'Home.html')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'Home.html')

        else:
            return render(request, 'signup.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'Home.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return render(request, 'Home.html')
        form = AuthenticationForm()
        return render(request, 'Login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'Login.html', {'form': form})


def home(request):
    return render(request, 'Home.html')


def signout(request):
    auth.logout(request)
    return redirect('/login/')
