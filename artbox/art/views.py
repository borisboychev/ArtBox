from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from art.forms import ArtForm, EditArtForm
from art.models import Art
from artbox_core.clean_up import clean_up
from artbox_core.decorators import denied_groups, required_groups
from users.models import UserProfile


class HomePageView(View):
    def get(self, request):
        return render(request, 'art_templates/home.html')


class GalleryView(View):
    def get(self, request):
        context = {
            'artwork': Art.objects.all(),
            'user': request.user,
        }

        return render(request, 'art_templates/gallery.html', context)


@required_groups(groups=['artist', 'admin'])
def delete_art(request, id):
    if request.method == "GET":
        art = Art.objects.get(id=id)
        if art.user.user == request.user:
            image = art.image
            clean_up(image.path)
            art.delete()
            return redirect('gallery page')
        return HttpResponse(f"Only user {art.user.user.username} is authorized to delete.")


@login_required(login_url='login')
@denied_groups(groups=['visitor'])
def create_art(request):
    if request.method == "GET":
        context = {
            'form': ArtForm(),
        }
        return render(request, 'art_templates/create.html', context)

    art_form = ArtForm(request.POST, request.FILES)
    if art_form.is_valid():

        user = UserProfile.objects.get(user=request.user)
        name = art_form.cleaned_data['name']
        artist = art_form.cleaned_data['artist']
        type = art_form.cleaned_data['type']
        image = art_form.cleaned_data['image']

        art = Art(name=name, artist=artist, type=type, image=image, user=user)
        art.save()

        return redirect('gallery page')
    else:
        context = {
            'form': ArtForm(),
        }
        return render(request, 'art_templates/create.html', context)


@required_groups(['artist', 'admin'])
def edit_art(request, id):
    art = Art.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'form': EditArtForm(),
        }

        if art.user.user != request.user:
            return HttpResponse(f"Only user {art.user.user.username} is authorized to delete.")

        return render(request, 'art_templates/edit.html', context)

    form = EditArtForm(request.POST)

    if form.is_valid():
        art_name = form.cleaned_data['name']
        artist = form.cleaned_data['artist']
        art_type = form.cleaned_data['type']

        # in case a field is empty it doesnt leave the field in the db empty
        if art_name:
            art.name = art_name

        if artist:
            art.artist = artist

        if art_type:
            art.type = art_type

        art.save()

        return redirect('gallery page')

    return render(request, 'art_templates/edit.html', {'form': EditArtForm()})
