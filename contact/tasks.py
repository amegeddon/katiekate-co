from django.core.mail import BadHeaderError, EmailMessage
from django.conf import settings
from background_task import background
import base64

# Background task function to send email
@background(schedule=10)
def send_email_task(subject, message, recipient_list, photo_base64=None, photo_name=None):
    try:
        email = EmailMessage(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list
        )

        # Attach the photo if provided
        if photo_base64 and photo_name:
            photo_data = base64.b64decode(photo_base64)
            email.attach(photo_name, photo_data, 'image/jpeg')  

        email.send(fail_silently=False)

    except BadHeaderError:
        print('Invalid header found.')
    except Exception as e:
        print(f"An error occurred: {e}")
