import datetime

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from api import models, serializers


class ApiTests(APITestCase):
    def auth(self):
        self.superuser = User.objects.create_superuser('test_user', 'test@user.com', 'test')
        self.client.login(username='test_user', password='test')
        token = Token.objects.get_or_create(user=self.superuser)
        self.client.force_authenticate(user=self.superuser, token=token)

    def setUp(self):
        self.classroom = models.ClassRoom.objects.create(number="A1")
        self.group = models.Group.objects.create(name="Group_1")
        self.student = models.Student.objects.create(fio="student test", email="student@test.com", group=self.group)
        self.lesson = models.Lesson.objects.create(
            name="Lesson_1",
            group=self.group,
            classroom=self.classroom,
            start_at=datetime.datetime(2021, 11, 29, 15, 0),
        )

    # Classrooms
    def test_classroom_list(self):
        url = reverse("classroom-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), models.ClassRoom.objects.count())

    def test_classroom_retrieve(self):
        url = reverse("classroom-detail", kwargs={"pk": self.classroom.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(serializers.ClassRoomSerializer(self.classroom).data))

    def test_classroom_update_with_auth(self):
        self.auth()
        url = reverse("classroom-detail", kwargs={"pk": self.classroom.pk})
        data = {"number": "A2"}
        response = self.client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.ClassRoom.objects.first().number, data.get("number"))

    def test_classroom_update_without_auth(self):
        url = reverse("classroom-detail", kwargs={"pk": self.classroom.pk})
        data = {"number": "A3"}
        response = self.client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_classroom_destroy_with_auth(self):
        self.auth()
        url = reverse("classroom-detail", kwargs={"pk": self.classroom.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.ClassRoom.objects.count(), 0)

    def test_classroom_destroy_without_auth(self):
        url = reverse("classroom-detail", kwargs={"pk": self.classroom.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_classroom_create_with_auth(self):
        self.auth()
        url = reverse("classroom-list")
        data = {"number": "A4"}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.ClassRoom.objects.last().number, data.get("number"))

    def test_classroom_create_without_auth(self):
        url = reverse("classroom-list")
        data = {"number": "A5"}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Groups
    def test_group_list(self):
        url = reverse("group-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), models.Group.objects.count())

    def test_group_retrieve(self):
        url = reverse("group-detail", kwargs={"pk": self.group.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(serializers.GroupSerializer(self.group).data))

    def test_group_update_with_auth(self):
        self.auth()
        url = reverse("group-detail", kwargs={"pk": self.group.pk})
        data = {"name": "Group_2"}
        response = self.client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Group.objects.first().name, data.get("name"))

    def test_group_update_without_auth(self):
        url = reverse("group-detail", kwargs={"pk": self.group.pk})
        data = {"name": "Group_2"}
        response = self.client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_group_destroy_with_auth(self):
        self.auth()
        url = reverse("group-detail", kwargs={"pk": self.group.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Group.objects.count(), 0)

    def test_group_destroy_without_auth(self):
        url = reverse("group-detail", kwargs={"pk": self.group.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_group_create_with_auth(self):
        self.auth()
        url = reverse("group-list")
        data = {"name": "Group_2"}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Group.objects.last().name, data.get("name"))

    def test_group_create_without_auth(self):
        url = reverse("group-list")
        data = {"name": "Group_2"}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_group_create_exists(self):
        self.auth()
        url = reverse("group-list")
        data = {"name": "Group_1"}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Students
    def test_student_list(self):
        url = reverse("student-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), models.Student.objects.count())

    def test_student_retrieve(self):
        url = reverse("student-detail", kwargs={"pk": self.student.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(serializers.StudentSerializer(self.student).data))

    def test_student_update_with_auth(self):
        self.auth()
        url = reverse("student-detail", kwargs={"pk": self.student.pk})
        data = {"fio": "jeff lebowski", "email": "jew@lebowski.com"}
        response = self.client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Student.objects.first().fio, data.get("fio"))
        self.assertEqual(models.Student.objects.first().email, data.get("email"))

    def test_student_update_without_auth(self):
        url = reverse("student-detail", kwargs={"pk": self.student.pk})
        data = {"fio": "jeff lebowski", "email": "jew@lebowski.com"}
        response = self.client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_student_destroy_with_auth(self):
        self.auth()
        url = reverse("student-detail", kwargs={"pk": self.student.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Student.objects.count(), 0)

    def test_student_destroy_without_auth(self):
        url = reverse("student-detail", kwargs={"pk": self.student.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_student_create_with_auth(self):
        self.auth()
        url = reverse("student-list")
        group = models.Group.objects.create(name="Group_3")
        data = {"fio": "jeff lebowski", "email": "jew@lebowski.com", "group": group.pk}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Student.objects.last().fio, data.get("fio"))
        self.assertEqual(models.Student.objects.last().email, data.get("email"))
        self.assertEqual(models.Student.objects.last().group, group)

    def test_student_create_without_auth(self):
        url = reverse("student-list")
        group = models.Group.objects.create(name="Group_3")
        data = {"fio": "jeff lebowski", "email": "jew@lebowski.com", "group": group.pk}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Lessons
    def test_lesson_list(self):
        url = reverse("lesson-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), models.Lesson.objects.count())

    def test_lesson_retrieve(self):
        url = reverse("lesson-detail", kwargs={"pk": self.lesson.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(serializers.LessonSerializer(self.lesson).data))

    def test_lesson_update_with_auth(self):
        self.auth()
        url = reverse("lesson-detail", kwargs={"pk": self.lesson.pk})
        data = {"name": "Lesson_2"}
        response = self.client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Lesson.objects.first().name, data.get("name"))

    def test_lesson_update_without_auth(self):
        url = reverse("lesson-detail", kwargs={"pk": self.lesson.pk})
        data = {"name": "Lesson_2"}
        response = self.client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_lesson_destroy_with_auth(self):
        self.auth()
        url = reverse("lesson-detail", kwargs={"pk": self.lesson.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Lesson.objects.count(), 0)

    def test_lesson_destroy_without_auth(self):
        url = reverse("lesson-detail", kwargs={"pk": self.lesson.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_lesson_create_with_auth(self):
        self.auth()
        url = reverse("lesson-list")
        group = models.Group.objects.create(name="Group_3")
        classroom = models.ClassRoom.objects.create(number="classroom_3")
        data = {
            "name": "Lesson_2",
            "start_at": datetime.datetime(2021, 11, 29, 13, 0),
            "classroom": classroom.pk,
            "group": group.pk
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Lesson.objects.last().name, data.get("name"))
        self.assertEqual(models.Lesson.objects.last().classroom, classroom)
        self.assertEqual(models.Lesson.objects.last().group, group)

    def test_lesson_create_without_auth(self):
        url = reverse("lesson-list")
        data = {"name": "Lesson_2"}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_lesson_create_exists(self):
        self.auth()
        url = reverse("lesson-list")
        data = {"name": "Lesson_1"}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)