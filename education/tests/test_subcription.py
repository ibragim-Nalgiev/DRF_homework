from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Course, Subscription
from users.models import User


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user_data = {'email': 'test_email@mail.com', "password": "1233456"}
        self.user = User.objects.create(**self.user_data)
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(title="test course")

    def test_create_subscription(self):
        subscription_data = {'user': self.user.pk, 'course': self.course.id}

        response = self.client.post(reverse('education:subscription_create'), data=subscription_data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

        self.assertEquals(response.json(), {'id': 1, 'user': self.user.pk, 'course': self.course.pk})

    def test_delete_subscription(self):
        subscription = Subscription.objects.create(user=self.user, course=self.course)
        response = self.client.delete(reverse('education:subscription_delete', kwargs={"pk": subscription.pk}))

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEquals(Subscription.objects.all().count(), 0)


