from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .tasks import send_email_task

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, files=request.FILES)  # Include request.FILES
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_content = form.cleaned_data['message']
            photo = request.FILES.get('photo')  # Get the photo from request.FILES

            subject = f"Contact Form Submission from {name}"
            message = f"Name: {name}<br>Email: {email}<br>Message: {message_content}"

            # Prepare email attachment if needed
            photo_file = photo if photo else None

            # Convert photo to base64 and pass it as a string
            photo_base64 = None
            if photo_file:
                import base64
                from io import BytesIO
                photo_file.seek(0)
                photo_base64 = base64.b64encode(photo_file.read()).decode('utf-8')

            # Schedule the background email task
            send_email_task(subject, message, ['katyKate@katy.com'], photo_base64, photo_file.name)
            print('task-started')

            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact/contact_success.html')
