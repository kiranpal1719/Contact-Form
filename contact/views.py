from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name    = form.cleaned_data['name']
            email   = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            success = True
            form = ContactForm()

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form,
        'success': success
    })
