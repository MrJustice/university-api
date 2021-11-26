import factory
from api import models


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Group

    name = factory.Sequence(lambda n: f"Group_{n}")


class ClassRoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ClassRoom

    number = factory.Sequence(lambda n: f"Classroom_{n}")


class LessonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Lesson

    name = factory.Sequence(lambda n: f"Lesson_{n}")

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.groups.add(extracted)


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Student

    fio = factory.Faker("name", locale="ru_RU")
    email = factory.LazyAttribute(lambda person: "{}@gmail.com".format("_".join(person.fio.split())))


