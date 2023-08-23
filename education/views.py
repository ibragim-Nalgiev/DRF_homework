from django.shortcuts import render

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .permissions import IsNotModerator, IsCourseOwner, IsModerator, IsLessonOwner
from .serializers import MyTokenObtainPairSerializer

from rest_framework import viewsets, mixins

from education.models import Course, Lesson
from education.serializers import CourseSerializer, LessonSerializer
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView


class CourseViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = CourseSerializer

    permission_classes_by_action = {
        'create': [IsNotModerator | IsAdminUser],
        'update': [IsCourseOwner | IsModerator | IsAdminUser],
        'partial_update': [IsCourseOwner | IsModerator | IsAdminUser],
        'destroy': [IsCourseOwner | IsAdminUser],
    }

    def get_queryset(self):

        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.groups.filter(
                name="Модераторы").exists():
            return Course.objects.all()

        return Course.objects.filter(course_owner=self.request.user)

    def get_permissions(self):
        if self.action in self.permission_classes_by_action:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        return [IsAuthenticated()]


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsNotModerator | IsAdminUser]

    def perform_create(self, serializer):
        new_lesson = serializer.save(lesson_owner=self.request.user)
        new_lesson.lesson_owner = self.request.user
        new_lesson.save()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.groups.filter(
                name="Модераторы").exists():
            return Lesson.objects.all()

        return Lesson.objects.filter(lesson_owner=self.request.user)


class LessonDetailAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsLessonOwner | IsModerator | IsAdminUser]
    serializer_class = LessonSerializer


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsLessonOwner | IsModerator | IsAdminUser]


class LessonDeleteAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsLessonOwner | IsAdminUser]







