
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from .forms import ImageEmailForm

def index(request):
    if request.method == 'POST':
        form = ImageEmailForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            image = form.cleaned_data['image']
            send_mail_with_image(email, image)
            return redirect('index')
    else:
        form = ImageEmailForm()
    return render(request, 'core/index.html', {'form': form})


def send_mail_with_image(email, image):
    email_subject = 'PryImg'
    email_body = f'Correo del remitente: {email}'
    email_from = 'jjv_83@hotmail.com'  # Reemplaza con tu correo
    email_to = [email]  # Utiliza la dirección de correo electrónico proporcionada

    email_message = EmailMessage(email_subject, email_body, email_from, email_to)
    email_message.attach(image.name, image.read(), image.content_type)
    email_message.send()