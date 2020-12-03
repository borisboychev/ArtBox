from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from art.forms import ContactUsForm


def home_page(request):
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