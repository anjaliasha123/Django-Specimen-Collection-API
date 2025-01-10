from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import SpeciesLocation

@shared_task
def notify_admins_and_process_put_request(notification):
        send_mail(
                'Update for INHS-HERP Data',
                f'Updation data: {notification[0]}\n\n Requester: {notification[1]}',
                'noreply@example.com',
                ["justforfun@example.com"],
        )
