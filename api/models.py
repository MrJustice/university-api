from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name="group name", max_length=5, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    fio = models.CharField(verbose_name="student FIO", max_length=50)
    email = models.EmailField(verbose_name="e-mail")
    group = models.ForeignKey(Group, related_name="students", on_delete=models.CASCADE)

    def __str__(self):
        return self.fio


class ClassRoom(models.Model):
    number = models.CharField(verbose_name="classroom number", max_length=5)


class Lesson(models.Model):
    name = models.CharField(verbose_name="Lesson name", max_length=50, unique=True)
    classroom = models.ForeignKey(ClassRoom, related_name="lessons", on_delete=models.SET_NULL, null=True)
    start_at = models.DateTimeField(verbose_name="lecture start time")
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.name
