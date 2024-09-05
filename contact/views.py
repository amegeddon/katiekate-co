from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import ContactForm
from .tasks import send_email_task

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_content = form.cleaned_data['message']

            subject = f"Contact Form Submission from {name}"
            message = f"Name: {name}\nEmail: {email}\nMessage: {message_content}"
            recipient_list = ['katyKate@katy.com']

            # Schedule the background email task
            send_email_task(subject, message, recipient_list)
            print('task-started')

            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact/contact_success.html')
