from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentsListApiView

app_name = PaymentConfig.name

urlpatterns = [
    path('payment', PaymentsListApiView.as_view(), name='payment'),
]