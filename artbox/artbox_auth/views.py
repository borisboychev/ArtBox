from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

# Create your views here.
from artbox_auth.forms import RegisterForm, LoginForm
from users.models import UserProfile


def register_user(request):
    if request.method == "GET":
        context = {
            'form': RegisterForm(),
        }
        return render(request, 'authentication_templates/register.html', context)

    register_form = RegisterForm(request.POST)

    if register_form.is_valid() and register_form.clean_email():
        user = register_form.save()

        # Every user gets visitor group by default
        starter_group = Group.objects.get(name='visitor')
        user.groups.add(starter_group)

        profile = UserProfile(user=user)
        profile.save()

        login(request, user)
        return redirect('gallery page')
    context = {
        'form': RegisterForm(),
    }
    return render(request, 'authentication_templates/register.html', context)


def login_user(request):
    if request.method == "GET":
        context = {
            'form': LoginForm(),
        }
        return render(request, 'authentication_templates/login.html', context)
    login_form = LoginForm(request.POST)

    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('gallery page')
        context = {
            'form': LoginForm(),
        }
        return render(request, 'authentication_templates/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('gallery page')
