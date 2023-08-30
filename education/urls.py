from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
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
    path('course/token/', MyObtainTokenPairView.as_view(), name='course_token'),
    path('lesson/token/', TokenObtainPairView.as_view(), name='lesson_token'),
    path('lesson/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('course/subscriptions/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('course/subscriptions/update/<int:pk>/', SubscriptionUpdateAPIView.as_view(), name='subscription_update'),
    path('course/subscriptions/', SubscriptionListAPIView.as_view(), name='subscription_list'),
    path('course/subscriptions/delete/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
] + router.urls


