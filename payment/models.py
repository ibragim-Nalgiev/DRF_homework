from django.db import models
from django.contrib.auth import get_user_model


class Payments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_course_or_lesson = models.CharField(max_length=200)
    sum = models.DecimalField(max_digits=20, decimal_places=2)
    way_of_pay = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user} {self.sum}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('-created_at',)




