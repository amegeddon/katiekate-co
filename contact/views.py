from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from .forms import ContactForm

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_content = form.cleaned_data['message']

        
            subject = f"Contact Form Submission from {name}"
            message = f"Name: {name}\nEmail: {email}\nMessage: {message_content}"

            # Setting the recipient email
            recipient_list = ['katyKate@katy.com']

            try:
                
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,  
                    recipient_list,  
                    fail_silently=False,  # Raise an error if email sending fails
                )
                
                return redirect('contact_success')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                # Logging or handling general exceptions (like SMTP errors)
                return HttpResponse(f"An error occurred: {e}")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact/contact_success.html')

