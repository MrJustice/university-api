import random
from faker import Faker

from django.db import transaction
from django.core.management import BaseCommand
from django.contrib.auth.models import User

from api.factories import StudentFactory, GroupFactory, ClassRoomFactory, LessonFactory, SuperUserFactory
from api.models import Student, Group, ClassRoom, Lesson


OBJECTS_COUNT = {"group": 5, "student": 20, "classroom": 15, "lesson": 75}
fake = Faker()


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        models = [Student, Group, Lesson, ClassRoom, User]
        if any(model.objects.exists() for model in models):
            self.stdout.write("Deleting previous data...")
            list(map(lambda model: model.objects.all().delete(), models))
            self.stdout.write("Deleting done!")

        self.stdout.write("Creating data...")

        SuperUserFactory()

        groups = []
        for _ in range(OBJECTS_COUNT["group"]):
            group = GroupFactory()
            groups.append(group)

        classrooms = []
        for _ in range(OBJECTS_COUNT["classroom"]):
            classroom = ClassRoomFactory()
            classrooms.append(classroom)

        for _ in range(OBJECTS_COUNT["student"]):
            StudentFactory(group=random.choice(groups))

        for _ in range(OBJECTS_COUNT["lesson"]):
            LessonFactory(
                group=random.choice(groups),
                classroom=random.choice(classrooms),
                start_at=fake.date_time_between(start_date='now', end_date='+1w'),
            )

        self.stdout.write("Creating done!")
