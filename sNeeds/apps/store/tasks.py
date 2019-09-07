from celery import shared_task, task

from django.utils import timezone

from sNeeds.utils import sendemail

from .models import SoldTimeSlotSale


@shared_task
def send_notify_sold_time_slot_mail(send_to, name, sold_time_slot_id):
    sendemail.notify_sold_time_slot(
        send_to,
        name,
        sold_time_slot_id
    )


@task()
def delete_time_slots():
    """
    Deletes time slots with less than 24 hours to start.
    """
    print("trying to delete")
    qs = SoldTimeSlotSale.objects.filter(start_time__lte=timezone.now() + timezone.timedelta(days=1))
    qs.delete()
