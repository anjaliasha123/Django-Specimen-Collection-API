from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import SpeciesLocation

@shared_task
def notify_admins_and_process_put_request(data):
        send_mail(
                'Update Request for SpeciesLocation Data',
                f'Request to update data: {data}',
                'noreply@example.com',
                ["justforfun@example.com"],
        )
        return data
