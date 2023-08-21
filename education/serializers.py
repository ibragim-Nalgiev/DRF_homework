from rest_framework import serializers, permissions

from education.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    course = serializers.ReadOnlyField(source='course.title')

    class Meta:
        model = Lesson
        permission_classes = [permissions.AllowAny]
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    lessons_info = LessonSerializer(source='course', many=True)

    def get_lessons_count(self, obj):
        return obj.lessons_set.all().count()

    def get_lessons(self, obj):
        return [el.pk for el in obj.lessons.all()]

    class Meta:
        model = Course
        permission_classes = [permissions.AllowAny]
        fields = '__all__'




