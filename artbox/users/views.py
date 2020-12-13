from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# Create your views here.
from artbox_core.clean_up import clean_up
from users.forms import UserProfileForm, EditProfileForm


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'profile/change-password.html'
    success_url = reverse_lazy('gallery page')


@login_required(login_url='login')
def edit_profile(request, id):
    if request.user.id != id:
        logout(request)
        return redirect('login')

    user = User.objects.get(id=id)
    if request.method == "GET":
        context = {
            'user': user,
            'form': EditProfileForm()
        }

        if request.user.id != user.id:
            return redirect('login')

        return render(request, 'profile/edit-profile.html', context)
    form = EditProfileForm(request.POST, request.FILES)
    if form.is_valid():
        print(form.errors)

        # checks if the profile didnt have an old picture
        if user.userprofile.profile_picture:
            old_pic = user.userprofile.profile_picture

            clean_up(old_pic.path)

        # in case a field is empty it doesnt leave the field in the db empty
        if form.cleaned_data['profile_picture']:
            user.userprofile.profile_picture = form.cleaned_data['profile_picture']

        if form.cleaned_data['username']:
            user.username = form.cleaned_data['username']

        if form.cleaned_data['email']:
            user.email = form.cleaned_data['email']

        user.save()
        user.userprofile.save()

        return redirect('profile page', id)


@login_required(login_url='login')
def profile_page(request, id):
    if request.user.id != id:
        logout(request)
        return redirect('login')

    user = User.objects.get(id=id)
    if request.method == "GET":
        context = {
            'user': user,
            'userprofile': user.userprofile,
            'artwork': user.userprofile.art_set.all(),
            'form': UserProfileForm()
        }

        return render(request, 'profile/profile-info.html', context)
