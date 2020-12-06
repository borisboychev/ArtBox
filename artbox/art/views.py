from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from art.forms import ContactUsForm
from art.models import Art


def home_page(request):
    # TODO: check if any user is logged in and make changes to navbar if true
    context = {
        'form': ContactUsForm(),
    }
    return render(request, 'home.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            first_name = request.POST('first_name')
            last_name = request.POST('last_name')
            email = request.POST('email')
            message = request.POST('message')
            send_mail(
                f'{first_name} {last_name}',
                message,
                email,
                ['borisboychev007@gmail.com'],
            )
        return redirect('home page')


def gallery(request):
    context = {
        'artwork': Art.objects.all()
    }

    return render(request, 'gallery.html', context)


def delete_art(request, id):
    if request.method == "GET":
        art = Art.objects.get(id=id)
        art.delete()
        return redirect('gallery page')