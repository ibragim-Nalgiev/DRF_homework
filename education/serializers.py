from rest_framework import serializers

from education.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons_set.all().count()

    def get_lessons(self, obj):
        return [el.pk for el in obj.lessons.all()]

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
