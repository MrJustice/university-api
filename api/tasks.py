import datetime

from django.contrib.postgres.aggregates import ArrayAgg
from django.core.mail import send_mass_mail

from api import models
from university import settings
from university.celery import app


@app.task
def send_schedule_to_email():
    tomorrow_day = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow_lessons = models.Lesson.objects.filter(
        start_at__range=[
            datetime.datetime.combine(tomorrow_day, datetime.time.min),
            datetime.datetime.combine(tomorrow_day, datetime.time.max)
        ]
    ).values("name", "classroom__number", "start_at", "group__name").annotate(emails=ArrayAgg("group__students__email"))

    if tomorrow_lessons:
        schedule = {lesson["group__name"]: {"emails": lesson["emails"], "lessons": []} for lesson in tomorrow_lessons}
        lessons_list = list(tomorrow_lessons)
        for i in lessons_list:
            schedule[i["group__name"]]["lessons"].append((i["name"], i["classroom__number"], i["start_at"]))

        message_title = "Your class schedule for tomorrow."
        for group_name, group_info in schedule.items():
            message_text = ""
            for index, lesson in enumerate(group_info["lessons"], start=1):
                message_text += f"{index}) {lesson[0]} (room {lesson[1]}) beginning at {lesson[2].strftime('%H:%M')} \n"
            data = (message_title, message_text, settings.EMAIL_HOST, group_info["emails"])
            email = send_mass_mail((data,), fail_silently=True)
            if email:
                print(f"Mail for the group {group_name} was sent successfully.")
            else:
                print(f"Mail for the group {group_name} wasn't sent.")
