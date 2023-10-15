from celery import shared_task

from .models import Email


@shared_task
def send_email(receiver_id: int):
    Email.objects.create(
        text='Подтвердите свою почту',
        receiver_id=receiver_id
    )
    print('Email was send')