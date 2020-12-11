from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from art.forms import ArtForm
from art.models import Art
from artbox_core.decorators import denied_groups, required_groups


def home_page(request):
    return render(request, 'art_templates/home.html')


def gallery(request):
    context = {
        'artwork': Art.objects.all()
    }

    return render(request, 'art_templates/gallery.html', context)


@required_groups(groups=['artist', 'admin'])
def delete_art(request, id):
    if request.method == "GET":
        art = Art.objects.get(id=id)
        art.delete()
        return redirect('gallery page')


@denied_groups(groups=['visitor'])
def create_art(request):
    if request.method == "GET":
        context = {
            'form': ArtForm(),
        }
        return render(request, 'art_templates/create.html', context)

    art_form = ArtForm(request.POST, request.FILES)
    print(art_form.is_valid())
    if art_form.is_valid():
        art_form.save()

        return redirect('gallery page')
    else:
        context = {
            'form': ArtForm(),
        }
        return render(request, 'art_templates/create.html', context)
