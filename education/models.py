from django.db import models
from django.contrib.auth import get_user_model


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




