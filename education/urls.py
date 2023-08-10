from django.urls import path
from rest_framework import routers

from education.apps import EducationConfig
from education.views import *

app_name = EducationConfig.name


router = routers.DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson_item'),
    path('lesson/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson_delete'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
] + router.urls


