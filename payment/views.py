from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payment.models import Payments
from payment.serializers import PaymentsSerializer


class PaymentsListApiView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course_or_lesson', 'way_of_pay')
    ordering_fields = ('created_at',)

