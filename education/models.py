from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='media/course/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    link_to_video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Владелец курса', null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='media/lesson/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    link_to_video = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    lesson_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Владелец урока', null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Курс', related_name='course', null=True)



    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = ' урок'
        verbose_name_plural = 'уроки'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='subscribed_user', on_delete=models.CASCADE,
                             related_name='subscribed_user')
    course = models.ForeignKey(Course, verbose_name='subscription_course', on_delete=models.CASCADE,
                               related_name='subscription_course')
    is_subscribed = models.BooleanField(default=False, verbose_name='Подписка осуществлена')

    def __str__(self):
        return f'{self.user} subscribed to {self.course}'

    class Meta:
        verbose_name = 'Подписка на курсы'
        verbose_name_plural = 'Подписки на курсы'
        ordering = ('course', 'is_subscribed')






