from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from background_task import background

# Background task function to send email
@background(schedule=10)
def send_email_task(subject, message, recipient_list):
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )
    except BadHeaderError:
        # Handle specific BadHeaderError here
        print('Invalid header found.')
    except Exception as e:
        # Handle general exceptions and log them
        print(f"An error occurred: {e}")
