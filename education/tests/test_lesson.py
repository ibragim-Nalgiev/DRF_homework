from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Course, Lesson
from users.models import User


class LessonCRUDTestCases(APITestCase):
    def setUp(self):
        self.user_data = {'email': 'test@mail.com', "password": "123786543"}
        self.user = User.objects.create(**self.user_data)
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="test course")

    def test_create_lesson(self):
        data = {"title": "test lesson", "link_to_video": 'https://youtube.com/lesson/',
                "course": self.course.id, "lesson_owner": self.user.pk}
        response = self.client.post(reverse('education:lesson_create'), data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEquals(
            response.json(),
            {'id': 1, 'title': 'test lesson', 'description': None, 'preview': None,
             'link_to_video': 'https://youtube.com/lesson/', 'course': 1, 'lesson_owner': 1}
        )

        self.assertEquals(Lesson.objects.all().count(), 1)

    def test_list_lesson(self):
        data = {"title": "test lesson", "link_to_video": 'https://youtube.com/lesson/2/',
                "course": self.course, "lesson_owner": self.user}
        lesson = Lesson.objects.create(**data)

        response = self.client.get(reverse('education:lesson_list'))

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(Lesson.objects.all().count(), 1)

    def test_update_lesson(self):
        data = {"title": "test lesson", "link_to_video": 'https://youtube.com/lesson/2/',
                "course": self.course, "lesson_owner": self.user}
        lesson = Lesson.objects.create(**data)
        new_data = {"title": "test lesson - UPDATED", "link_to_video": 'https://youtube.com/lesson/2/new/',
                    "course": self.course.pk, "lesson_owner": self.user.pk}

        response = self.client.put(reverse('education:lesson_update', kwargs={"pk": lesson.pk}), data=new_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {'id': lesson.pk, 'title': 'test lesson - UPDATED', 'description': None, 'preview': None,
             'link_to_video': 'https://youtube.com/lesson/2/new/', 'course': self.course.pk,
             'lesson_owner': self.user.pk})

    def test_partial_update_lesson(self):
        data = {"title": "test lesson", "link_to_video": 'https://youtube.com/lesson/',
                "course": self.course, "lesson_owner": self.user}
        lesson = Lesson.objects.create(**data)
        new_data = {"title": "test lesson - UPDATED", "link_to_video": 'https://youtube.com/lesson/new/'}

        response = self.client.patch(reverse('education:lesson_update', kwargs={"pk": lesson.pk}), data=new_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {'id': lesson.pk, 'title': 'test lesson - UPDATED', 'description': None, 'preview': None,
             'link_to_video': 'https://youtube.com/lesson/new/', 'course': self.course.pk,
             'lesson_owner': self.user.pk})

    def test_retrieve_lesson(self):
        data = {"title": "test lesson", "link_to_video": 'https://youtube.com/lesson/',
                "course": self.course, "lesson_owner": self.user}
        lesson = Lesson.objects.create(**data)

        response = self.client.get(reverse('education:lesson_item', kwargs={"pk": lesson.pk}))

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(
            response.json(),
            {'title': 'test lesson', 'description': None, 'preview': None,
             'link_to_video': 'https://youtube.com/lesson/', 'course': "test course"}
        )

    def test_delete_lesson(self):
        data = {"title": "test lesson", "link_to_video": 'https://youtube.com/lesson/',
                "course": self.course, "lesson_owner": self.user}
        lesson = Lesson.objects.create(**data)

        response = self.client.delete(reverse('education:lesson_delete', kwargs={"pk": lesson.pk}))

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEquals(Lesson.objects.all().count(), 0)
