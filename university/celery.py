import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "university.settings")

app = Celery("university")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send_tomorrow_schedule": {
        "task": "api.tasks.send_schedule_to_email",
        "schedule": crontab(hour=19, minute=0, day_of_week=[0, 1, 2, 3, 4, 6]),
    },
}

if __name__ == "__main__":
    app.start()