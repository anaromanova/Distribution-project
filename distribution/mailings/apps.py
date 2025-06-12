# mailings/apps.py

from django.apps import AppConfig

class MailingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailings'

    def ready(self, django_celery_beat=None):
        from django_celery_beat.models import PeriodicTask, IntervalSchedule
        from django.utils.timezone import now
        import json

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.MINUTES,
        )

        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Send scheduled mailings',
            task='mailings.tasks.send_scheduled_mailings',
            defaults={'start_time': now(), 'enabled': True, 'kwargs': json.dumps({})}
        )

