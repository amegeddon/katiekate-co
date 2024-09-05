from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse
from templated_mail.mail import BaseEmailMessage

def contact_page(request):
    try:
      message = BaseEmailMessage(
          template_name='emails/hello.html', 
          context = {'name': 'Amy'}
      )
      message.send(['katyKate@katy.com'])
    except BadHeaderError:
        pass
    return render(request, 'contact.html', {'name': 'amy'})
