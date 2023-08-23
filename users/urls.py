from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserListCreateView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user'),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenObtainPairView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
