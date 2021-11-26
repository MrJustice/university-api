import factory
from api import models

from django.contrib.auth.models import User


class SuperUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = 'admin@admin.com'
    username = 'admin'
    password = factory.PostGenerationMethodCall('set_password', 'admin')
    is_staff = True
    is_active = True
    is_superuser = True


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Group

    name = factory.Sequence(lambda n: f"Group_{n+1}")


class ClassRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ClassRoom

    number = factory.Sequence(lambda n: f"Classroom_{n+1}")


class LessonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Lesson

    name = factory.Sequence(lambda n: f"Lesson_{n+1}")

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.groups.add(extracted)


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Student

    fio = factory.Faker("name", locale="ru_RU")
    email = factory.LazyAttribute(lambda person: "{}@gmail.com".format("_".join(person.fio.lower().split())))


